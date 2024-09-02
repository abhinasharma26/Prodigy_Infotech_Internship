import selenium
from selenium import webdriver
url = 'https://www.youtube.com/watch?v=YrwRd_27fhw&list=RDYrwRd_27fhw&start_radio=1'


driver = webdriver.Chrome()
driver.get(url)