from dataclasses import dataclass

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
    raw_volume: int = 0  # Daily volume for raw item
    cooked_volume: int = 0  # Daily volume for cooked item 