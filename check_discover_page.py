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

class check_discover_page(unittest.TestCase):
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

    def test_2_go_to_discover_page(self):
        # find "discover" button and click
        wait.until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='drawer']/a[1]"))).click()
        # check "discover" page
        # check URl
        self.assertIn("http://localhost:5279/?discover", self.driver.current_url)
        # check title in header
        self.assertIn("Discover", self.driver.find_element_by_xpath(".//*[@id='header']/div/h1").get_attribute("textContent"))
        # check title in right sidebar
        self.assertIn("drawer-item drawer-item-selected",
                      self.driver.find_element_by_xpath(".//*[@id='drawer']/a[1]").get_attribute("class"))

        # check page content
        a = 1
        while a < 6:
            list_of_files = self.driver.find_element_by_xpath(".//*[@id='main-content']/main/div/div[1]/div[" + str(a) +"]/section")
            self.assertTrue((list_of_files).is_displayed())
            a += 1

        b = 1
        while b < 6:
            list_of_files = self.driver.find_element_by_xpath(".//*[@id='main-content']/main/div/div[2]/div[" + str(b) +"]/section")
            self.assertTrue((list_of_files).is_displayed())
            b += 1


    def test_3_check_card(self):
        # check pictures in card
        self.assertTrue(self.driver.find_element_by_xpath(".//*[@id='main-content']/main/div/div[1]/div[1]/section/div/div[1]/a/img")
                        .is_displayed())

        # card header is displayed
        self.assertTrue(self.driver.find_element_by_xpath(".//*[@id='main-content']/main/div/div[1]/div[1]/section/div/div[2]/div[1]")
                        .is_displayed())

        # card title is displayed
        self.assertTrue(self.driver.find_element_by_xpath(".//*[@id='main-content']/main/div/div[1]/div[1]/section/div/div[2]/h3")
                        .is_displayed())

    def test_4_left_sidebar(self):
        self.assertIn("Close", self.driver.find_element_by_xpath(".//*[@id='drawer-handle']/a[1]")
                      .get_attribute("title"))
        self.driver.find_element_by_xpath(".//*[@id='drawer-handle']/a[1]").click()
        self.assertIsNot("Close", self.driver.find_element_by_xpath(".//*[@id='drawer-handle']/a[1]")
                      .get_attribute("title"))

        self.driver.find_element_by_xpath(".//*[@id='header']/div/a/span[1]").click()
        self.assertIn("Close", self.driver.find_element_by_xpath(".//*[@id='drawer-handle']/a[1]")
                      .get_attribute("title"))


    def test_5_check_search(self):
        # find search field
        search_field = self.driver.find_element_by_xpath(".//*[@id='header']/div/div/input")
        self.assertIn("Find movies, music, games, and more", search_field.get_attribute("placeholder"))

        search_field.click()
        search_field.clear()
        search_field.send_keys("aabbc")

        # check lst of result
        a = 1
        while a < 15:
            list_result = self.driver.find_element_by_xpath(".//*[@id='main-content']/main/div/section[" + str(a) + "]")
            self.assertTrue((list_result).is_displayed())
            a += 1

        # check firs result
        self.assertIn("Test 10MB Upload",
                      self.driver.find_element_by_xpath(".//*[@id='main-content']/main/div/section[1]/div/div[2]/h3/a/span")
                      .get_attribute("textContent"))

        # check price
        """self.assertIn("0",
                      self.driver.find_element_by_xpath(".//*[@id='main-content']/main/div/section[1]/div/div[2]/span/span/span[1]/span[1]")
                      .get_attribute("textContent"))"""

    def test_6_file_page(self):
        # go to file page
        self.driver.find_element_by_xpath(".//*[@id='main-content']/main/div/section[1]/div/div[2]/h3/a/span").click()
        # check page
        # check url
        self.assertIn("http://localhost:5279/?show=aabbc", self.driver.current_url)
        # check title
        self.assertIn("lbry://aabbc", self.driver.find_element_by_xpath(".//*[@id='header']/div/h1").get_attribute("textContent"))
        # check card
        self.assertTrue(self.driver.find_element_by_xpath(".//*[@id='main-content']/main/section").is_displayed())
        # check card title
        self.assertIn("Test 10MB Upload", self.driver.find_element_by_xpath(".//*[@id='main-content']/main/section/div/h2")
                      .get_attribute("textContent"))

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    if __name__ == '__main__':
        unittest.main()

