import selenium
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

url = 'https://www.amazon.in/Decorative-India-Protection-Ayurveda-Benefits/dp/B0D3XT1MJ3'

driver.get(url)

try:
    product_name = driver.find_element(By.ID, 'productTitle').text
except:
    product_name = "N/A"

try:
    product_price = driver.find_element(By.XPATH, '//span[@id="priceblock_ourprice"]').text
except:
    try:
        product_price = driver.find_element(By.XPATH, '//span[@id="priceblock_dealprice"]').text
    except:
        product_price = "N/A"

try:
    product_rating = driver.find_element(By.XPATH, '//span[@data-asin="B0D3XT1MJ3"]').get_attribute("aria-label")
except:
    product_rating = "N/A"

driver.quit()

with open('amazon_product_info.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Product Name', 'Price', 'Rating'])
    writer.writerow([product_name, product_price, product_rating])

print("Data has been written to amazon_product_info.csv")