from cooking_item import CookingItem
from cooking_profit_calculator import CookingProfitCalculator


def main():
    calculator = CookingProfitCalculator()
    # Get cooking level from user
    try:
        cooking_level_input = input("Enter your cooking level (1-99) [default: 99]: ").strip()
        cooking_level = int(cooking_level_input) if cooking_level_input else 99
        if not 1 <= cooking_level <= 99:
            raise ValueError("Cooking level must be between 1 and 99")
    except ValueError as e:
        print(f"Invalid input: {e}")
        cooking_level = 99
        print("Defaulting to level 99")
    # Get sort preference
    print("\nSort by:")
    print("1. Profit (default)")
    print("2. ROI (Return on Investment)")
    print("3. XP")
    try:
        sort_choice_input = input("Enter your choice (1-3) [default: 1]: ").strip()
        sort_choice = int(sort_choice_input) if sort_choice_input else 1
        sort_options = {1: "profit", 2: "roi", 3: "xp"}
        sort_by = sort_options.get(sort_choice, "profit")
    except ValueError:
        sort_by = "profit"
        print("Invalid choice, defaulting to profit sorting")
    # Run analysis
    calculator.print_analysis(cooking_level, sort_by)

if __name__ == "__main__":
    main() 