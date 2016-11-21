import unittest, time,re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

class check_myfiles_page(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.title
        cls.driver.get("http://localhost:5279/")
        global wait
        wait = WebDriverWait(cls.driver, 15)

    def test_1_check_download_apge(self):
        # find "My files" button and click
        wait.until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='drawer']/a[3]"))).click()
        # check url
        self.assertIn("http://localhost:5279/?downloaded", self.driver.current_url)
        # check header title
        self.assertIn("My Files",
                      self.driver.find_element_by_xpath(".//*[@id='header']/div/h1")
                      .get_attribute("textContent"))

        # check subheader
        self.assertIn("sub-header-selected", self.driver.find_element_by_xpath(".//*[@id='header']/nav/a[1]").get_attribute("class"))

    def test_2_check_published_page(self):
        # find "Published" button and click
        wait.until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='header']/nav/a[2]"))).click()
        # check url
        self.assertIn("http://localhost:5279/?published", self.driver.current_url)
        # check header title
        self.assertIn("My Files",
                      self.driver.find_element_by_xpath(".//*[@id='header']/div/h1")
                      .get_attribute("textContent"))

        # check subheader
        self.assertIn("sub-header-selected", self.driver.find_element_by_xpath(".//*[@id='header']/nav/a[2]").get_attribute("class"))


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    if __name__ == '__main__':
        unittest.main()