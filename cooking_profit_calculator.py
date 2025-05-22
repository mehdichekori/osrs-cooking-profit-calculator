import requests
import time
from datetime import datetime
from typing import Dict, List
from cooking_item import CookingItem

class CookingProfitCalculator:
    def __init__(self):
        self.API_URL = "https://prices.runescape.wiki/api/v1/osrs/latest"
        self.VOLUME_URL = "https://prices.runescape.wiki/api/v1/osrs/volumes"
        self.CACHE_DURATION = 300  # 5 minutes cache
        self.last_cache_time = 0
        self.last_volume_cache_time = 0
        self.price_cache: Dict[int, int] = {}
        self.volume_cache: Dict[int, int] = {}
        # Enhanced item data with cooking levels and XP
        self.item_data = [
            {"name": "Karambwan", "raw_id": 3142, "cooked_id": 3144, "burn_level": 99, "cooking_xp": 190},
            {"name": "Shark", "raw_id": 383, "cooked_id": 385, "burn_level": 94, "cooking_xp": 210},
            {"name": "Sea turtle", "raw_id": 395, "cooked_id": 397, "burn_level": 82, "cooking_xp": 211.3},
            {"name": "Manta ray", "raw_id": 389, "cooked_id": 391, "burn_level": 91, "cooking_xp": 216.2},
            {"name": "Anglerfish", "raw_id": 13439, "cooked_id": 13441, "burn_level": 84, "cooking_xp": 230},
            {"name": "Moon antelope", "raw_id": 29113, "cooked_id": 29143, "burn_level": 99, "cooking_xp": 220},
            {"name": "Sun antelope", "raw_id": 29116, "cooked_id": 29140, "burn_level": 95, "cooking_xp": 175},
            {"name": "Dark crab", "raw_id": 11934, "cooked_id": 11936, "burn_level": 99, "cooking_xp": 215},
            {"name": "Monkfish", "raw_id": 7944, "cooked_id": 7946, "burn_level": 92, "cooking_xp": 120},
            {"name": "Lobster", "raw_id": 377, "cooked_id": 379, "burn_level": 74, "cooking_xp": 120},
            {"name": "Swordfish", "raw_id": 371, "cooked_id": 373, "burn_level": 86, "cooking_xp": 140},
            {"name": "Tuna", "raw_id": 359, "cooked_id": 361, "burn_level": 65, "cooking_xp": 100},
            {"name": "Salmon", "raw_id": 331, "cooked_id": 329, "burn_level": 58, "cooking_xp": 90},
            {"name": "Dashing kebbit", "raw_id": 10132, "cooked_id": 10134, "burn_level": 89, "cooking_xp": 200},
            {"name": "Pyre fox", "raw_id": 28367, "cooked_id": 28369, "burn_level": 80, "cooking_xp": 180},
            {"name": "Larupia", "raw_id": 10095, "cooked_id": 10097, "burn_level": 82, "cooking_xp": 199.5}
        ]

    def _should_refresh_cache(self) -> bool:
        return time.time() - self.last_cache_time > self.CACHE_DURATION

    def _should_refresh_volume_cache(self) -> bool:
        return time.time() - self.last_volume_cache_time > self.CACHE_DURATION

    def _fetch_prices(self) -> None:
        try:
            response = requests.get(self.API_URL, timeout=10)
            response.raise_for_status()
            data = response.json()
            for item in self.item_data:
                raw_id, cooked_id = str(item["raw_id"]), str(item["cooked_id"])
                if raw_id in data["data"] and cooked_id in data["data"]:
                    self.price_cache[item["raw_id"]] = data["data"][raw_id]["low"]
                    self.price_cache[item["cooked_id"]] = data["data"][cooked_id]["low"]
            self.last_cache_time = time.time()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching prices: {e}")
            if not self.price_cache:
                raise

    def _fetch_volumes(self) -> None:
        try:
            headers = {"User-Agent": "osrs-cooking-profit-calc/1.0 (contact: your_email@example.com)"}
            response = requests.get(self.VOLUME_URL, headers=headers, timeout=10)
            response.raise_for_status()
            data = response.json()
            for item_id, volume in data["data"].items():
                self.volume_cache[int(item_id)] = volume
            self.last_volume_cache_time = time.time()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching volumes: {e}")
            if not self.volume_cache:
                raise

    def calculate_profits(self, cooking_level: int = 99) -> List[CookingItem]:
        if self._should_refresh_cache():
            self._fetch_prices()
        if self._should_refresh_volume_cache():
            self._fetch_volumes()
        cooking_items = []
        for item in self.item_data:
            raw_price = self.price_cache.get(item["raw_id"])
            cooked_price = self.price_cache.get(item["cooked_id"])
            raw_volume = self.volume_cache.get(item["raw_id"], 0)
            cooked_volume = self.volume_cache.get(item["cooked_id"], 0)
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
                cooking_xp=item["cooking_xp"],
                raw_volume=raw_volume,
                cooked_volume=cooked_volume
            ))
        return cooking_items

    def print_analysis(self, cooking_level: int = 99, sort_by: str = "profit") -> None:
        try:
            items = self.calculate_profits(cooking_level)
            sort_keys = {
                "profit": lambda x: x.profit,
                "roi": lambda x: x.roi,
                "xp": lambda x: x.cooking_xp
            }
            items.sort(key=sort_keys.get(sort_by, sort_keys["profit"]), reverse=True)
            print("\n" + "=" * 120)
            print(f"OSRS Cooking Profit Analysis - Level {cooking_level}")
            print(f"Prices updated: {datetime.fromtimestamp(self.last_cache_time)}")
            print("=" * 120)
            print(f"{'Item':<15} | {'Raw Price':>10} | {'Cooked Price':>12} | {'Profit':>8} | {'ROI':>7} | {'XP':>7} | {'Burn Lvl':>8} | {'Raw Vol':>10} | {'Cooked Vol':>11} | {'Status':>10}")
            print("-" * 120)
            for item in items:
                can_cook = cooking_level >= item.burn_level
                status = "✓ Can cook" if can_cook else "✗ Too high"
                print(f"{item.name:<15} | {item.raw_price:>10,d} | {item.cooked_price:>12,d} | {item.profit:>8,d} | {item.roi:>6.1f}% | {item.cooking_xp:>7.1f} | {item.burn_level:>8d} | {item.raw_volume:>10,d} | {item.cooked_volume:>11,d} | {status:>10}")
            print("\n" + "=" * 120)
            best_profit = max(items, key=lambda x: x.profit)
            best_roi = max(items, key=lambda x: x.roi)
            best_xp = max(items, key=lambda x: x.cooking_xp)
            print(f"Best profit: {best_profit.name} (Buy raw: {best_profit.raw_price:,d}, Sell cooked: {best_profit.cooked_price:,d}, Profit: {best_profit.profit:,d} coins)")
            print(f"Best ROI: {best_roi.name} (Buy raw: {best_roi.raw_price:,d}, Sell cooked: {best_roi.cooked_price:,d}, ROI: {best_roi.roi:.1f}%)")
            print(f"Best XP: {best_xp.name} (Buy raw: {best_xp.raw_price:,d}, Sell cooked: {best_xp.cooked_price:,d}, XP: {best_xp.cooking_xp} xp)")
            print("=" * 120 + "\n")
        except Exception as e:
            print(f"Error during analysis: {e}") 