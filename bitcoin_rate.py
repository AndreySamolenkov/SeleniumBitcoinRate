from datetime import datetime
import time
import csv
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


options = Options()
options.add_experimental_option('detach', True)

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)


driver.get('https://finance.yahoo.com/quote/BTC-USD')

# Open the CSV file in write mode
with open('data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)

    # Write the header row
    writer.writerow(['date', 'price (USD)'])

    # Loop to write new rows to the CSV file every 60 seconds
    for _ in range(5):
        # Get the current date and time
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")

        # Get the Bitcoin price from the webpage
        elem = driver.find_element(
            By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[6]/div/div/div/div[3]/div[1]/div/fin-streamer[1]')
        price = elem.text

        # Write the current date and time and Bitcoin price to a new row in the CSV file
        writer.writerows([[current_time, price]])
        print(f'As of {current_time} the price is ${price}')

        # Wait for 60 seconds and then refresh the webpage
        time.sleep(60)
        driver.refresh()

print('Done')
# Close the browser
driver.quit()
