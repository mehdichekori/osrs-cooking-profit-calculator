import requests

# List of item pairs (raw_id, cooked_id, name)
item_pairs = [
    (3142, 3144, "Karambwan"),
    (383, 385, "Shark"),
    (395, 397, "Sea turtle"),
    (389, 391, "Manta ray"),
    (13439, 13441, "Anglerfish")
]

def get_item_price_from_api(item_id):
    try:
        url = f"https://prices.runescape.wiki/api/v1/osrs/latest"
        response = requests.get(url)
        data = response.json()
        # Assuming item_id is the key for the raw and cooked item prices
        raw_price = data["data"].get(str(item_id[0]), {}).get("low")
        cooked_price = data["data"].get(str(item_id[1]), {}).get("low")
        return raw_price, cooked_price
    except Exception as e:
        print(f"Error fetching data for item {item_id}: {e}")
        return None, None

def calculate_cooking_profit(raw_price, cooked_price, name):
    try:
        raw_price = int(raw_price)
        cooked_price = int(cooked_price)
        profit = cooked_price - raw_price
        print(f"{name}s|Raw Price: {raw_price}, Cooked Price: {cooked_price}, Profit: {profit} coins.")
        return name, profit, raw_price, cooked_price
    except Exception as e:
        print(f"Error calculating profit for {name}: {e}")
        return None

def main():
    profits = []
    for raw_id, cooked_id, name in item_pairs:
        raw_price, cooked_price = get_item_price_from_api((raw_id, cooked_id))
        if raw_price is not None and cooked_price is not None:
            result = calculate_cooking_profit(raw_price, cooked_price, name)
            if result:
                profits.append(result)
        else:
            print(f"Unable to fetch prices for {name}")

    if profits:
        most_profitable = max(profits, key=lambda x: x[1])
        most_profitable_name, most_profitable_profit, most_profitable_raw_price, most_profitable_cooked_price = most_profitable
        print(f"\nThe most profitable item to cook are {most_profitable_name}s with a profit of {most_profitable_profit} coins.")
        print(f"Buy raw {most_profitable_name}s for {most_profitable_raw_price}, sell cooked {most_profitable_name}s for {most_profitable_cooked_price} coins.")
        print("\n")
    else:
        print("\nUnable to determine the most profitable item due to data retrieval issues.")

if __name__ == "__main__":
    main()