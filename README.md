Readme for web scraping code to extract Bitcoin price from Yahoo Finance

This Python script uses Selenium to extract the current price of Bitcoin in USD from the Yahoo Finance website and save it to a CSV file.
Prerequisites

    Python 3
    selenium library
    ChromeDriver for Selenium, which can be downloaded from the following link and placed in the same directory as the script: https://sites.google.com/a/chromium.org/chromedriver/downloads

Usage

    Run the script using a Python interpreter
    The script opens a Chrome browser window and navigates to the Yahoo Finance webpage for Bitcoin
    The script then creates a new CSV file with the name data.csv and writes the header row with columns date and price (USD)
    The script then runs a loop to extract the Bitcoin price from the webpage and write a new row to the CSV file every 60 seconds. The loop runs for 5 iterations.
    The script prints the current date and time, along with the Bitcoin price, to the console.
    When the loop is finished, the script closes the browser and prints "Done" to the console.

Output

    The output of the script is a CSV file called data.csv containing two columns: date and price (USD). Each row contains the current date and time, and the current price of Bitcoin in USD as extracted from the Yahoo Finance webpage.

Note

    This script is for educational purposes only and should not be used for any illegal or unauthorized activities. The author does not accept responsibility for any actions taken by the user.
