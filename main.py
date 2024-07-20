from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    return webdriver.Chrome(options=chrome_options)

def get_item_price(driver, item_id):
    url = f"https://prices.runescape.wiki/osrs/item/{item_id}"
    driver.get(url)
    try:
        price_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.wgl-item-price'))
        )
        return int(price_element.text.replace(',', '').split()[0])
    except Exception as e:
        print(f"Error fetching data for item {item_id}: {e}")
        return None

def calculate_cooking_profit(driver, raw_id, cooked_id):
    raw_price = get_item_price(driver, raw_id)
    cooked_price = get_item_price(driver, cooked_id)
    
    if raw_price is not None and cooked_price is not None:
        profit = cooked_price - raw_price
        return profit
    else:
        return None

# List of item pairs (raw_id, cooked_id, name)
item_pairs = [
    (3142, 3144, "Karambwan"),
    (383, 385, "Shark"),
    (395, 397, "Sea turtle"),
    (389, 391, "Manta ray"),
    (13439, 13441, "Anglerfish")
]

driver = setup_driver()
profits = []

try:
    for raw_id, cooked_id, name in item_pairs:
        profit = calculate_cooking_profit(driver, raw_id, cooked_id)
        if profit is not None:
            print(f"Profit for cooking {name}: {profit} coins")
            profits.append((name, profit))
        else:
            print(f"Unable to calculate profit for {name}")
        
        time.sleep(1)  # Add a delay to avoid overwhelming the server

    if profits:
        most_profitable = max(profits, key=lambda x: x[1])
        print(f"\nThe most profitable item to cook is {most_profitable[0]} with a profit of {most_profitable[1]} coins.")
    else:
        print("\nUnable to determine the most profitable item due to data retrieval issues.")
finally:
    driver.quit()