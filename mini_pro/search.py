from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.youtube.com/")
print(driver.title)

search = driver.find_element_by_id("search")
search.send_keys("test")
search.send_keys(Keys.RETURN)
time.sleep(5)
