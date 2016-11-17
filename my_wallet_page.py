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

class check_wallet_page(unittest.TestCase):
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

    def test_2_go_to_My_wallet_page(self):
        # find "My Wallet" button and click
        wait.until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='drawer']/a[4]"))).click()
        # check url
        self.assertIn("http://localhost:5279/?wallet", self.driver.current_url)
        # check header title
        self.assertIn("My Wallet",
                      self.driver.find_element_by_xpath(".//*[@id='header']/div/h1")
                      .get_attribute("textContent"))

    def test_3_check_overview_page(self):
        # check "overview" is selected
        self.assertIn("sub-header-selected", self.driver.find_element_by_xpath(".//*[@id='header']/nav/a[1]")
                      .get_attribute("class"))

        # check cards
        a = 1
        while a < 3:
            cards_list = self.driver.find_element_by_xpath(".//*[@id='main-content']/main/section[" + str(a) + "]")
            self.assertTrue((cards_list).is_displayed())
            a += 1

        # check Balance card
        self.assertIn("Balance", self.driver.find_element_by_xpath(".//*[@id='main-content']/main/section[1]/h3")
                      .get_attribute("textContent"))

        #check Transaction card
        self.assertIn("Transaction History", self.driver.find_element_by_xpath(".//*[@id='main-content']/main/section[2]/h3")
                      .get_attribute("textContent"))


    def test_4_check_send_page(self):
        # check "send" is selected
        self.driver.find_element_by_xpath(".//*[@id='header']/nav/a[2]").click()
        self.assertIn("sub-header-selected", self.driver.find_element_by_xpath(".//*[@id='header']/nav/a[2]")
                      .get_attribute("class"))

        # check cards
        a = 1
        while a < 3:
            cards_list = self.driver.find_element_by_xpath(".//*[@id='main-content']/main/section[" + str(a) + "]")
            self.assertTrue((cards_list).is_displayed())
            a += 1

        # check Balance card
        self.assertIn("Balance", self.driver.find_element_by_xpath(".//*[@id='main-content']/main/section[1]/h3")
                      .get_attribute("textContent"))

        #check Transaction card
        self.assertIn("Send Credits", self.driver.find_element_by_xpath(".//*[@id='main-content']/main/section[2]/form/h3")
                      .get_attribute("textContent"))

    def test_5_check_Receive_page(self):
        # check "Receive" is selected
        self.driver.find_element_by_xpath(".//*[@id='header']/nav/a[3]").click()
        self.assertIn("sub-header-selected", self.driver.find_element_by_xpath(".//*[@id='header']/nav/a[3]")
                      .get_attribute("class"))

        # check cards
        a = 1
        while a < 3:
            cards_list = self.driver.find_element_by_xpath(".//*[@id='main-content']/main/section[" + str(a) + "]")
            self.assertTrue((cards_list).is_displayed())
            a += 1

        # check Balance card
        self.assertIn("Balance", self.driver.find_element_by_xpath(".//*[@id='main-content']/main/section[1]/h3")
                      .get_attribute("textContent"))

        #check Transaction card
        self.assertIn("Wallet Address", self.driver.find_element_by_xpath(".//*[@id='main-content']/main/section[2]/h3")
                      .get_attribute("textContent"))


    def test_6_check_claim_beta_code_page(self):
        # check "Claim Beta Code" is selected
        self.driver.find_element_by_xpath(".//*[@id='header']/nav/a[4]").click()
        self.assertIn("sub-header-selected", self.driver.find_element_by_xpath(".//*[@id='header']/nav/a[4]")
                      .get_attribute("class"))

        # check cards
        self.assertTrue((self.driver.find_element_by_xpath(".//*[@id='main-content']/main/form/div")).is_displayed())

        self.assertIn("Claim your beta invitation code", self.driver.find_element_by_xpath(".//*[@id='main-content']/main/form/div/h2")
                      .get_attribute("textContent"))


    def test_7_check_check_referral_credit_page(self):
        # check "Check Referral Credit" is selected
        self.driver.find_element_by_xpath(".//*[@id='header']/nav/a[5]").click()
        self.assertIn("sub-header-selected", self.driver.find_element_by_xpath(".//*[@id='header']/nav/a[5]")
                      .get_attribute("class"))

        # check cards
        self.assertTrue((self.driver.find_element_by_xpath(".//*[@id='main-content']/main/form/div")).is_displayed())

        self.assertIn("Check your referral credits", self.driver.find_element_by_xpath(".//*[@id='main-content']/main/form/div/h2")
                      .get_attribute("textContent"))



    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    if __name__ == '__main__':
        unittest.main()