# OSRS Cooking Profit Calculator

## Project Goals
This project helps Old School RuneScape (OSRS) players maximize their profit from cooking by:
- Fetching real-time Grand Exchange prices and daily trade volumes for raw and cooked food items using the OSRS Wiki API.
- Calculating profit, ROI, and XP for each item, and showing how realistic it is to buy/sell based on daily volume.
- Presenting a clear, sortable table to help you choose the best item to cook for your level and goals.

## Features
- Real-time price and volume data from the OSRS Wiki API
- Calculates profit, ROI, and XP for each cookable item
- Shows daily trade volume for both raw and cooked items
- Sort results by profit, ROI, or XP
- User-friendly CLI
- Modular, maintainable codebase

## Available Foods
The following foods are currently analyzed by this tool:
- Karambwan
- Shark
- Sea turtle
- Manta ray
- Anglerfish
- Moon antelope
- Sun antelope
- Dark crab
- Monkfish
- Lobster
- Swordfish
- Tuna
- Salmon
- Dashing kebbit
- Pyre fox
- Larupia

## ⚠️ Deprecated Folder
**Do not use anything in the `Deprecated/` folder.**
- The scripts and files in `Deprecated/` are not maintained and may not work with the current API or codebase.
- All current and future development is in the main project root (see below).

## Code Structure
- `scrape-api-v2.py`: Main script and CLI entrypoint. Handles user input and runs the analysis.
- `cooking_item.py`: Defines the `CookingItem` dataclass (structure for each food item and its stats).
- `cooking_profit_calculator.py`: Contains the `CookingProfitCalculator` class, which fetches data, calculates profits, and prints the analysis table.
- `Deprecated/`: Old scripts, not maintained. **Do not use.**

## Installation & Setup
1. **Clone the repository:**
    ```bash
    git clone https://github.com/mehdichekori/osrs-cooking-profit-calculator.git
    cd osrs-cooking-profit-calculator
    ```
2. **(Recommended) Create and activate a virtual environment:**
    ```bash
    python -m venv myenv
    # On Windows:
    myenv\Scripts\activate
    # On macOS/Linux:
    source myenv/bin/activate
    ```
3. **Install dependencies:**
    ```bash
    pip install requests
    ```
    (If you want to use Selenium-based scripts for web scraping, also run:)
    ```bash
    pip install selenium
    ```
4. **(Optional) Download ChromeDriver** if you want to use Selenium scripts (not required for main tool).

## Usage
### Main CLI Tool (Recommended)
Run the main script:
```bash
python main.py
```
- Enter your cooking level (1-99) when prompted (or press Enter for 99).
- Choose how to sort the results: Profit, ROI, or XP.
- The tool will print a table with prices, profit, ROI, XP, burn level, and daily volumes for each item.

### Example Output
```
========================================================================================================================
OSRS Cooking Profit Analysis - Level 99
Prices updated: 2025-05-22 12:34:28.014013
========================================================================================================================
Item            |  Raw Price | Cooked Price |   Profit |     ROI |      XP | Burn Lvl |    Raw Vol |  Cooked Vol |     Status
------------------------------------------------------------------------------------------------------------------------
Moon antelope   |      3,551 |        3,997 |      446 |   12.6% |   220.0 |       99 |    307,052 |     489,644 | ✓ Can cook
Manta ray       |      1,300 |        1,700 |      400 |   30.8% |   216.2 |       91 |    746,090 |   2,094,931 | ✓ Can cook
Sun antelope    |        431 |          804 |      373 |   86.5% |   175.0 |       95 |    100,650 |     106,298 | ✓ Can cook
Monkfish        |        236 |          582 |      346 |  146.6% |   120.0 |       92 |  2,521,332 |   2,568,969 | ✓ Can cook
Anglerfish      |      1,424 |        1,759 |      335 |   23.5% |   230.0 |       84 |  4,712,621 |   4,875,878 | ✓ Can cook
Sea turtle      |        665 |          997 |      332 |   49.9% |   211.3 |       82 |    431,215 |     357,003 | ✓ Can cook
Shark           |        602 |          861 |      259 |   43.0% |   210.0 |       94 |  8,341,947 |   6,291,445 | ✓ Can cook
Dark crab       |      1,064 |        1,260 |      196 |   18.4% |   215.0 |       99 |    338,224 |     779,827 | ✓ Can cook
Lobster         |         68 |          179 |      111 |  163.2% |   120.0 |       74 |  5,192,693 |   4,031,726 | ✓ Can cook
Karambwan       |        351 |          452 |      101 |   28.8% |   190.0 |       99 |  5,533,256 |   4,395,571 | ✓ Can cook
Swordfish       |         77 |          167 |       90 |  116.9% |   140.0 |       86 |  4,007,884 |   2,258,129 | ✓ Can cook
Tuna            |         54 |          115 |       61 |  113.0% |   100.0 |       65 |  1,420,737 |   1,001,796 | ✓ Can cook
Salmon          |         53 |           77 |       24 |   45.3% |    90.0 |       58 |    731,938 |     485,502 | ✓ Can cook
Larupia         |        401 |            5 |     -396 |  -98.8% |   199.5 |       82 |        909 |         184 | ✓ Can cook
Dashing kebbit  |      2,853 |        2,150 |     -703 |  -24.6% |   200.0 |       89 |        178 |           2 | ✓ Can cook
========================================================================================================================
Best profit: Moon antelope (Buy raw: 3,551, Sell cooked: 3,997, Profit: 446 coins)
Best ROI: Lobster (Buy raw: 68, Sell cooked: 179, ROI: 163.2%)
Best XP: Anglerfish (Buy raw: 1,424, Sell cooked: 1,759, XP: 230 xp)
========================================================================================================================
```

## Contributing
- Issues and pull requests are welcome!
- Please do not submit changes to the Deprecated folder.
- For new features or bugfixes, work with the modular code in the project root.

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Disclaimer
This tool is for educational purposes only. Use it responsibly and ensure compliance with the terms of service of websites from which data is fetched, such as the OSRS Wiki. Always check and comply with the website's robots.txt file and terms of use.
