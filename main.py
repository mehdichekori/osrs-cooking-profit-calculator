import requests
from bs4 import BeautifulSoup
import time

def get_item_price(item_id):
    url = f"https://prices.runescape.wiki/osrs/item/{item_id}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # You'll need to replace this selector with the correct one for the buy price
    price_element = soup.select_one('.buy-price-value')
    
    if price_element:
        return int(price_element.text.replace(',', ''))
    else:
        return None

def calculate_cooking_profit(raw_id, cooked_id):
    raw_price = get_item_price(raw_id)
    cooked_price = get_item_price(cooked_id)
    
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

profits = []

for raw_id, cooked_id, name in item_pairs:
    profit = calculate_cooking_profit(raw_id, cooked_id)
    if profit is not None:
        print(f"Profit for cooking {name}: {profit} coins")
        profits.append((name, profit))
    else:
        print(f"Unable to calculate profit for {name}")
    
    # Add a delay to avoid overwhelming the server
    time.sleep(1)

if profits:
    most_profitable = max(profits, key=lambda x: x[1])
    print(f"\nThe most profitable item to cook is {most_profitable[0]} with a profit of {most_profitable[1]} coins.")
else:
    print("\nUnable to determine the most profitable item due to data retrieval issues.")