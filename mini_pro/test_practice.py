import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Test:
    def test_setUp(self):
        url = "http://dev-1.aiti-kace.com.gh:8075/"
        PATH = "C:\Program Files (x86)\chromedriver.exe"
        self.driver_service = Service(executable_path=PATH)
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
        self.driver.get(url)
        self.driver.maximize_window()
        # assert url == "http://dev-1.aiti-kace.com.gh:8075/"

        email = "admin@test.com"
        password = "password"
        self.driver.find_element(By.ID, "email").send_keys(email)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.CLASS_NAME, "login").send_keys(Keys.RETURN)
        # print("Logged In Successfully")


        self.driver.find_element(By.CSS_SELECTOR, "[href='http://dev-1.aiti-kace.com.gh:8075/visitors/index']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[href='http://dev-1.aiti-kace.com.gh:8075/visitors/create']").click()


        # FILL THE FORM
        name = "Willui"
        contact = "0587930281"
        address = "Tema"
        purpose = "To see my sister"
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "name"))).send_keys(name)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "contact"))).send_keys(contact)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "address"))).send_keys(address)
        gen = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "gender")))
        Select(gen).select_by_index(1)
        dep = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "department")))
        Select(dep).select_by_index(1)
        staff = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "selectStaff")))
        Select(staff).select_by_index(1)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "purpose"))).send_keys(purpose)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Submit')]"))).click()
        assert name in self.driver.page_source
        time.sleep(20)
        # tbody = self.driver.find_element(By.XPATH, '//*[@id="myTable"]/tbody')
        # data = []
        # for tr in tbody.find_elements(By.XPATH, '//*[@id="myTable"]/tbody/tr'):
        #     row = [item.text for item in tr.find_elements(By.XPATH, '//*[@id="myTable"]/tbody/tr/td')]
        #     data.append(row)
        # # print(data)
        # assert name in data
        # table = self.driver.find_element(By.ID, "myTable")
        # header = table.find_elements(By.TAG_NAME, "th")
        # for headerEl in header:
        #     print(headerEl.text)
        # body = table.find_element(By.TAG_NAME, "tbody")

        # cells = body.find_elements(By.TAG_NAME, "td")

        # for cell in cells:
        #     print(cell.text)
        #     assert "Kojo" in self.driver.page_source



    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()







# a = driver.find_element(By.ID, "name").send_keys(name)
# b = driver.find_element(By.NAME, "contact").send_keys(contact)
# c = driver.find_element(By.NAME, "address").send_keys(address)
# d = Select(driver.find_element(By.ID, 'gender')).select_by_index(2)
# e = Select(driver.find_element(By.ID, 'department')).select_by_index(2)
# f = Select(driver.find_element(By.ID, 'selectStaff')).select_by_index(2)
# g = driver.find_element(By.NAME, "purpose").send_keys(purpose)







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
