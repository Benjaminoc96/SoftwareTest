import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

email = "admin@test.com"
password = "password"
url = "http://dev-1.aiti-kace.com.gh:8075/"
driver_service = Service(executable_path="C:\Program Files (x86)\chromedriver.exe")
PATH = "C:\Program Files (x86)\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.get(url)
driver.maximize_window()
elem = driver.find_element(By.ID, "email")
elem.send_keys(email)
lem = driver.find_element(By.ID, "password")
lem.send_keys(password)
em = driver.find_element(By.CLASS_NAME, "login")
em.send_keys(Keys.RETURN)
print("Logged In Successfully")

# INTERACTING WITH WEBPAGE
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.clear()
# elem.send_keys(" and some", Keys.RETURN)
# elem.send_keys(Keys.ARROW_DOWN)
# assert "No results found." not in driver.page_source
# driver.close()

# PRINTING THE OPTIONS IN A DROPDOWN MENU
# driver.get(url)
# element = driver.find_element(By.NAME, "gender")
# all_options = element.find_elements(By.TAG_NAME, "option")
# for option in all_options:
#     print("Value is: %s" % option.get_attribute("value"))
#     option.click()

# SELECTING AN OPTION FROM THE DROPDOWN MENU BY INDEX
# from selenium.webdriver.support.ui import Select
# select = Select(driver.find_element(By.NAME, 'gender'))
# select.select_by_index(2)
# select.select_by_visible_text("Female")

# DESELECTING AN OPTION
# select = Select(driver.find_element(By.NAME, 'gender'))
# select.deselect_all()

# SUBMIT
