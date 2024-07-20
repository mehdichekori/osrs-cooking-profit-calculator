from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def setup_driver():
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
        return driver
    except Exception as e:
        print(f"Error initializing WebDriver: {e}")
        return None

def get_item_price(driver, item_id):
    try:
        url = f"https://prices.runescape.wiki/osrs/item/{item_id}"
        driver.get(url)
        price_element = WebDriverWait(driver, 2,).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.wgl-item-price'))
        )
        return int(price_element.text.replace(',', '').split()[0])
    
    except Exception as e:
        print(f"Error fetching data for item {item_id}: {e}")
    return None

def calculate_cooking_profit(driver, raw_id, cooked_id, name):
    raw_price = get_item_price(driver, raw_id)
    cooked_price = get_item_price(driver, cooked_id)
    
    if raw_price is not None and cooked_price is not None:
        profit = cooked_price - raw_price
        print(f"{name}|Raw Price: {raw_price}, Cooked Price: {cooked_price}, Profit: {profit} coins.")
        return name, profit, raw_price, cooked_price
    else:
        print(f"Unable to calculate profit for {name}")
        return None

# List of item pairs (raw_id, cooked_id, name)
item_pairs = [
    (3142, 3144, "Karambwan"),
    (383, 385, "Shark"),
    (395, 397, "Sea turtle"),
    (389, 391, "Manta ray"),
    (13439, 13441, "Anglerfish")
]

def main():
    driver = setup_driver()
    if driver is None:
        print("Failed to initialize WebDriver. Exiting.")
        return
    
    profits = []
    for raw_id, cooked_id, name in item_pairs:
        result = calculate_cooking_profit(driver, raw_id, cooked_id, name)
        if result:
            profits.append(result)
    
    driver.quit()
    
    if profits:
        most_profitable = max(profits, key=lambda x: x[1])
        most_profitable_name, most_profitable_profit, most_profitable_raw_price, most_profitable_cooked_price = most_profitable
        
        print(f"\n{most_profitable_name} is the most profitable fish to cook with a profit of {most_profitable_profit} coins per fish.")

        print(f"Buy raw {most_profitable_name} for {most_profitable_raw_price}, sell cooked {most_profitable_name} for {most_profitable_cooked_price} coins. \n")
    else:
        print("\nUnable to determine the most profitable item due to data retrieval issues.")

if __name__ == "__main__":
    main()
