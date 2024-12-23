import requests

# List of item pairs (raw_id, cooked_id, name)
item_pairs = [
    (3142, 3144, "Karambwan"),
    (383, 385, "Shark"),
    (395, 397, "Sea turtle"),
    (389, 391, "Manta ray"),
    (13439, 13441, "Anglerfish"),
    (377, 379, "Lobster"),
    (371, 373, "Sword Fish"),
    (359, 361, "Tuna")
]

def get_item_price_from_api(item_id):
    try:
        url = "https://prices.runescape.wiki/api/v1/osrs/latest"
        response = requests.get(url)
        data = response.json()
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
        roi = (profit / raw_price) * 100 if raw_price != 0 else 0
        return name, profit, raw_price, cooked_price, roi
    except Exception as e:
        print(f"Error calculating profit for {name}: {e}")
        return None

def print_profit_info(item_info):
    name, profit, raw_price, cooked_price, roi = item_info
    print(f"{name} | Raw Price: {raw_price}, Cooked Price: {cooked_price}, Profit: {profit} coins, ROI: {roi:.2f}%")

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
        # Sort profits list by profit value (index 1) in descending order
        sorted_profits = sorted(profits, key=lambda x: x[1], reverse=True)
        
        # Print all items in sorted order
        print("\nAll cooking profits sorted by profit (highest to lowest):")
        print("=" * 70)
        for item_info in sorted_profits:
            print_profit_info(item_info)
        
        # Get the most profitable item (first item in sorted list)
        most_profitable = sorted_profits[0]
        most_profitable_name, most_profitable_profit, most_profitable_raw_price, most_profitable_cooked_price, most_profitable_roi = most_profitable
        
        print("\n" + "=" * 70)
        print(f"{most_profitable_name} is the most profitable fish to cook with a profit of {most_profitable_profit} coins per fish and ROI of {most_profitable_roi:.2f}%.")
        print(f"Buy raw {most_profitable_name} for {most_profitable_raw_price}, sell cooked {most_profitable_name} for {most_profitable_cooked_price} coins.")
        print("=" * 70 + "\n")
    else:
        print("\nUnable to determine the most profitable item due to data retrieval issues.")

if __name__ == "__main__":
    main()