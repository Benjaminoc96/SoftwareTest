from selenium.webdriver import Keys

import xcel
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver_service = Service(executable_path=PATH)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
url = 'https://www.amazon.com'
driver.get(url)
path = "C:/Users/Lenovo/Desktop/testandsee.xlsx"
rows = xcel.getRowCount(path, 'Sheet1')
for r in range(2, rows + 1):
    name = xcel.readData(path, 'Sheet1', r, 1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="twotabsearchtextbox"]'))).send_keys(name)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="nav-search-submit-button"]'))).click()
try:
    assert name in driver.page_source
    print('test passed')
    xcel.writeData(path, 'Sheet1', r, 4, 'test passed')
except AssertionError:
    print('test failed')
    xcel.writeData(path, 'Sheet1', r, 4, 'test failed')
