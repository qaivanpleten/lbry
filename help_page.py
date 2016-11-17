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

class check_help_page(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.title
        cls.driver.get("http://localhost:5279/")
        global wait
        wait = WebDriverWait(cls.driver, 15)

    # def test_1_check_starting_page(self):
    #     # check url
    #     self.assertIn("http://localhost:5279/?claim", self.driver.current_url)
    #     # check "Claim your beta invitation code" popup is displayed
    #     self.assertTrue(self.driver.find_element_by_xpath(
    #         ".//*[@id='main-content']/main/form/div").is_displayed())
    #     # check "Claim Beta Code" is selected
    #     self.assertIn("sub-header-selected", self.driver.find_element_by_xpath(".//*[@id='header']/nav/a[4]").get_attribute("class"))

    def test_2_check_settings_page(self):
        # find "help" button and click
        wait.until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='drawer']/a[6]"))).click()
        # check url
        self.assertIn("http://localhost:5279/?help", self.driver.current_url)
        # check header title
        self.assertIn("Help",
                      self.driver.find_element_by_xpath(".//*[@id='header']/div/h1")
                      .get_attribute("textContent"))

    def test_3_check_page_content(self):
        # check cards
        a = 1
        while a < 5:
            cards_list = self.driver.find_element_by_xpath("//*[@id='main-content']/main/section[" + str(a) + "]")
            self.assertTrue((cards_list).is_displayed())
            a += 1

        # check "Read the FAQ" title and button
        self.assertIn("Read the FAQ", self.driver.find_element_by_xpath(".//*[@id='main-content']/main/section[1]/h3").
                      get_attribute("textContent"))
        self.assertTrue((self.driver.find_element_by_xpath(".//*[@id='main-content']/main/section[1]/p[2]/a")).is_displayed())

        # check "Get Live Help" title and button
        self.assertIn("Get Live Help", self.driver.find_element_by_xpath(".//*[@id='main-content']/main/section[2]/h3").
                      get_attribute("textContent"))
        self.assertTrue((self.driver.find_element_by_xpath(".//*[@id='main-content']/main/section[2]/p[2]/a")).is_displayed())

        # check "Report a Bug" title and button
        self.assertIn("Report a Bug", self.driver.find_element_by_xpath(".//*[@id='main-content']/main/section[3]/h3").
                      get_attribute("textContent"))
        self.assertTrue((self.driver.find_element_by_xpath(".//*[@id='main-content']/main/section[3]/p[2]/a")).is_displayed())



    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    if __name__ == '__main__':
        unittest.main()