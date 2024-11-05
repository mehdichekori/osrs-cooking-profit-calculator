import requests
from datetime import datetime
import json
from typing import Dict, List, Tuple, Optional
import time
from dataclasses import dataclass
import sys
from concurrent.futures import ThreadPoolExecutor

@dataclass
class CookingItem:
    name: str
    raw_id: int
    cooked_id: int
    raw_price: int
    cooked_price: int
    profit: int
    roi: float
    burn_level: int  # Level where you stop burning
    cooking_xp: float  # XP gained per successful cook

class CookingProfitCalculator:
    def __init__(self):
        self.API_URL = "https://prices.runescape.wiki/api/v1/osrs/latest"
        self.CACHE_DURATION = 300  # 5 minutes cache
        self.last_cache_time = 0
        self.price_cache: Dict[int, int] = {}
        
        # Enhanced item data with cooking levels and XP
        self.item_data = [
            {
                "name": "Karambwan",
                "raw_id": 3142,
                "cooked_id": 3144,
                "burn_level": 99,
                "cooking_xp": 190
            },
            {
                "name": "Shark",
                "raw_id": 383,
                "cooked_id": 385,
                "burn_level": 94,
                "cooking_xp": 210
            },
            {
                "name": "Sea turtle",
                "raw_id": 395,
                "cooked_id": 397,
                "burn_level": 82,
                "cooking_xp": 211.3
            },
            {
                "name": "Manta ray",
                "raw_id": 389,
                "cooked_id": 391,
                "burn_level": 91,
                "cooking_xp": 216.2
            },
            {
                "name": "Anglerfish",
                "raw_id": 13439,
                "cooked_id": 13441,
                "burn_level": 84,
                "cooking_xp": 230
            }
        ]

    def _should_refresh_cache(self) -> bool:
        """Check if the cache needs refreshing"""
        return time.time() - self.last_cache_time > self.CACHE_DURATION

    def _fetch_prices(self) -> None:
        """Fetch all prices from the API and update cache"""
        try:
            response = requests.get(self.API_URL, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            # Update cache with new prices
            for item in self.item_data:
                raw_id, cooked_id = str(item["raw_id"]), str(item["cooked_id"])
                if raw_id in data["data"] and cooked_id in data["data"]:
                    self.price_cache[item["raw_id"]] = data["data"][raw_id]["low"]
                    self.price_cache[item["cooked_id"]] = data["data"][cooked_id]["low"]
            
            self.last_cache_time = time.time()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching prices: {e}")
            if not self.price_cache:  # Only raise if we have no cached data
                raise

    def calculate_profits(self, cooking_level: int = 99) -> List[CookingItem]:
        """Calculate profits for all items based on current prices and cooking level"""
        if self._should_refresh_cache():
            self._fetch_prices()
        
        cooking_items = []
        for item in self.item_data:
            raw_price = self.price_cache.get(item["raw_id"])
            cooked_price = self.price_cache.get(item["cooked_id"])
            
            if raw_price is None or cooked_price is None:
                continue
                
            profit = cooked_price - raw_price
            roi = (profit / raw_price * 100) if raw_price > 0 else 0
            
            cooking_items.append(CookingItem(
                name=item["name"],
                raw_id=item["raw_id"],
                cooked_id=item["cooked_id"],
                raw_price=raw_price,
                cooked_price=cooked_price,
                profit=profit,
                roi=roi,
                burn_level=item["burn_level"],
                cooking_xp=item["cooking_xp"]
            ))
            
        return cooking_items

    def print_analysis(self, cooking_level: int = 99, sort_by: str = "profit") -> None:
        """Print profit analysis with various sorting options"""
        try:
            items = self.calculate_profits(cooking_level)
            
            # Sorting options
            sort_keys = {
                "profit": lambda x: x.profit,
                "roi": lambda x: x.roi,
                "xp": lambda x: x.cooking_xp
            }
            
            items.sort(key=sort_keys.get(sort_by, sort_keys["profit"]), reverse=True)
            
            # Print header
            print("\n" + "=" * 100)
            print(f"OSRS Cooking Profit Analysis - Level {cooking_level}")
            print(f"Prices updated: {datetime.fromtimestamp(self.last_cache_time)}")
            print("=" * 100)
            
            # Print table header
            print(f"{'Item':<15} | {'Raw Price':>10} | {'Cooked Price':>12} | {'Profit':>8} | {'ROI':>7} | {'XP':>7} | {'Burn Lvl':>8} | {'Status':>10}")
            print("-" * 100)
            
            # Print each item
            for item in items:
                can_cook = cooking_level >= item.burn_level
                status = "✓ Can cook" if can_cook else "✗ Too high"
                
                print(f"{item.name:<15} | {item.raw_price:>10,d} | {item.cooked_price:>12,d} | {item.profit:>8,d} | {item.roi:>6.1f}% | {item.cooking_xp:>7.1f} | {item.burn_level:>8d} | {status:>10}")
            
            # Print summary
            print("\n" + "=" * 100)
            best_profit = max(items, key=lambda x: x.profit)
            best_roi = max(items, key=lambda x: x.roi)
            best_xp = max(items, key=lambda x: x.cooking_xp)
            
            print(f"Best profit: {best_profit.name} ({best_profit.profit:,d} coins)")
            print(f"Best ROI: {best_roi.name} ({best_roi.roi:.1f}%)")
            print(f"Best XP: {best_xp.name} ({best_xp.cooking_xp} xp)")
            print("=" * 100 + "\n")
            
        except Exception as e:
            print(f"Error during analysis: {e}")

def main():
    calculator = CookingProfitCalculator()
    
    # Get cooking level from user
    try:
        cooking_level = int(input("Enter your cooking level (1-99): ").strip())
        if not 1 <= cooking_level <= 99:
            raise ValueError("Cooking level must be between 1 and 99")
    except ValueError as e:
        print(f"Invalid input: {e}")
        cooking_level = 99
        print("Defaulting to level 99")
    
    # Get sort preference
    print("\nSort by:")
    print("1. Profit")
    print("2. ROI (Return on Investment)")
    print("3. XP")
    try:
        sort_choice = int(input("Enter your choice (1-3): ").strip())
        sort_options = {1: "profit", 2: "roi", 3: "xp"}
        sort_by = sort_options.get(sort_choice, "profit")
    except ValueError:
        sort_by = "profit"
        print("Invalid choice, defaulting to profit sorting")
    
    # Run analysis
    calculator.print_analysis(cooking_level, sort_by)

if __name__ == "__main__":
    main()