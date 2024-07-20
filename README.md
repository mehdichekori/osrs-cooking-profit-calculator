# OSRS Cooking Profit Calculator

## Description
This Python project calculates the profit margins for cooking various food items in Old School RuneScape (OSRS). It fetches real-time price data from the OSRS Wiki API and determines the most profitable food item to cook based on current prices.

## Features
- Fetches real-time price data from the OSRS Wiki API
- Calculates profit margins for cooking different food items
- Determines the most profitable food item to cook
- Includes two scripts for different data retrieval methods:
  - `scrape-api.py`: Fetches data directly from the OSRS Wiki API, faster and efficient for price updates.
  - `scrape-ui.py`: Uses Selenium for web scraping, suitable for dynamically loaded content from the OSRS Wiki.


## Food Items Analyzed
- Karambwan
- Shark
- Sea turtle
- Manta ray
- Anglerfish

## Example Output
- Karambwan | Raw Price: 413, Cooked Price: 527, Profit: 114 coins, ROI: 27.60%
- Shark | Raw Price: 700, Cooked Price: 805, Profit: 105 coins, ROI: 15.00%
- Sea turtle | Raw Price: 815, Cooked Price: 1010, Profit: 195 coins.
- Manta ray | Raw Price: 1250, Cooked Price: 1496, Profit: 246 coins, ROI: 19.68%
- Anglerfish | Raw Price: 2096, Cooked Price: 2101, Profit: 5 coins, ROI: 0.24%
###
- Manta ray is the most profitable fish to cook with a profit of 246 coins per fish and ROI of 19.68%.
- Buy raw Manta ray for 1250, sell cooked Manta ray for 1496 coins.

## Prerequisites
- Python 3.x
- Google Chrome browser
- `selenium` library (`pip install selenium`)
- `requests` library (`pip install requests`)

## Installation

1. Clone this repository:
    ```
    git clone https://github.com/mehdichekori/osrs-cooking-profit-calculator.git
    cd osrs-cooking-profit-calculator
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```bash
    python -m venv myenv
    ```
    - On Windows
    ```
    myenv\Scripts\activate
    ```
    - On macOS and Linux
    ```
    source myenv/bin/activate
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Download ChromeDriver:
   - Visit https://sites.google.com/chromium.org/driver/downloads
   - Download the version matching your Chrome browser
   - Extract `chromedriver.exe` and place it in the project directory.

## Usage

### Using `scrape-ui.py` (Selenium-based script)

- Ensure ChromeDriver is in the project directory.
- Run the script:
    ```bash
    python3 scrape-ui.py
    ```
  
### Using `scrape-api.py` (API-based script)

- Faster and recommended for regular use.
- Run the script:
    ```bash
    python3 scrape-api.py
    ```

Both scripts will output the profit for cooking each food item and recommend the most profitable option based on the fetched prices.

## Contributing
Contributions, issues, and feature requests are welcome. Feel free to check the [issues page](https://github.com/mehdichekori/osrs-cooking-profit-calculator/issues) if you want to contribute.

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/mehdichekori/osrs-cooking-profit-calculator/blob/main/LICENSE) file for details.

## Disclaimer
This tool is for educational purposes only. Use it responsibly and ensure compliance with the terms of service of websites from which data is fetched, such as the OSRS Wiki. Always check and comply with the website's robots.txt file and terms of use.
