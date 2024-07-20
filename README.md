# OSRS Cooking Profit Calculator

## Description
This Python script calculates the profit margins for cooking various food items in Old School RuneScape (OSRS). It scrapes real-time price data from the OSRS Wiki and determines the most profitable food item to cook based on current Grand Exchange prices.

## Features
- Scrapes real-time price data from the OSRS Wiki
- Calculates profit margins for cooking different food items
- Determines the most profitable food item to cook
- Uses Selenium for web scraping, allowing it to handle dynamically loaded content

## Food Items Analyzed
- Karambwan
- Shark
- Sea turtle
- Manta ray
- Anglerfish

## Prerequisites
- Python 3.x
- Google Chrome browser

## Installation

1. Clone this repository:
    ```
    https://github.com/mehdichekori/osrs-cooking-profit-calculator.git
    ```
2. Navigate to the folder
    ```
    cd osrs-cooking-profit-calc
    ```
  
3. Create a virtual environment:
    ```
    python -m venv myenv
    ```

4. Activate the virtual environment:
- On Windows:
  ```
  myenv\Scripts\activate
  ```
- On macOS and Linux:
  ```
  source myenv/bin/activate
  ```

5. Install the required packages:
    ```
    pip install selenium requests beautifulsoup4
    ```
  
5. Download ChromeDriver:
- Go to https://sites.google.com/chromium.org/driver/downloads
- Download the version that matches your Chrome browser version
- Extract the `chromedriver.exe` file and place it in the same directory as the script

## Usage

- Run the script:
    ```
    python3 main.py
    ```
    
The script will output the profit for cooking each food item and recommend the most profitable option.

## Contributing
Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/mehdichekori/osrs-cooking-profit-calculator/issues) if you want to contribute.

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Disclaimer
This tool is for educational purposes only. Be aware that web scraping may be against the OSRS Wiki's terms of service. Always check and comply with the website's robots.txt file and terms of use.