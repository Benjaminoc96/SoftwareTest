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
        url = "http://dev-1.aiti-kace.com.gh:7071/"
        PATH = "C:\Program Files (x86)\chromedriver.exe"
        self.driver_service = Service(executable_path=PATH)
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
        self.driver.get(url)
        self.driver.maximize_window()


        email = "superadmin@test.com"
        password = "admintest"
        self.driver.find_element(By.ID, "mat-input-0").send_keys(email)
        self.driver.find_element(By.ID, "mat-input-1").send_keys(password)
        self.driver.find_element(By.CLASS_NAME, "mdc-button__label").click()


        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div/mat-sidenav-container/mat-sidenav/div/app-sidebar/div/mat-nav-list/app-sidebar-item[2]/mat-list-item/span/span"))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div/mat-sidenav-container/mat-sidenav/div/app-sidebar/div/mat-nav-list/app-sidebar-item[2]/mat-nav-list/mat-list-item[2]/span/span/a"))).click()



        # DELETE PRINCIPAL
        principal_name = "Demot"
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='dataTable']/mat-row[13]/mat-cell[4]/button[2]"))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='mat-mdc-dialog-0']/div/div/app-confirm-dialog/div[2]/button[2]"))).click()
        time.sleep(5)
        assert principal_name in self.driver.page_source



    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()