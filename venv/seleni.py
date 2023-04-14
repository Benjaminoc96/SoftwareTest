from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

driver_service = Service(executable_path="C:\Program Files (x86)\chromedriver.exe")

PATH = "C:\Program Files (x86)\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=options, service=driver_service)

driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.amazon.com/")

search_box = driver.find_element("id", "twotabsearchtextbox")
search_box.send_keys('Dan Brown books')
search_box.send_keys(Keys.RETURN)

# search_box.submit()
# time.sleep(5)
try:
    search = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "s-desktop-width-max s-desktop-content s-wide-grid-style-t1 s-opposite-dir s-wide-grid-style sg-row"))
    )
    print(search.text)
    driver.close()
except:
    driver.quit()

