import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time







class Employee(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        PATH = 'C:\Program Files (x86)\chromedriver.exe'
        cls.driver_service = Service(executable_path=PATH)
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)
        cls.driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
        cls.driver.maximize_window()

    def test_valid(self):
        url = 'http://127.0.0.1:8000/login'
        self.driver.get(url)
        email = 'admin@test.com'
        password = 'password'
        self.driver.find_element(By.ID, 'form2Example17').send_keys(email)
        self.driver.find_element(By.ID, 'form2Example27').send_keys(password)
        self.driver.find_element(By.CLASS_NAME, 'btn btn-dark btn-lg btn-block').click()
        time.sleep(20)
        assert 'Add Employee' in self.driver.page_source

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        print('Test Completed')


if __name__ == "__main__":
    unittest.main()
