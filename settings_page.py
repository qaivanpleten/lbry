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

class check_settings_page(unittest.TestCase):
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
        # find "settings" button and click
        wait.until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='drawer']/a[5]"))).click()
        # check url
        self.assertIn("http://localhost:5279/?settings", self.driver.current_url)
        # check header title
        self.assertIn("Settings",
                      self.driver.find_element_by_xpath(".//*[@id='header']/div/h1")
                      .get_attribute("textContent"))

        # check cards
        a = 1
        while a < 6:
            cards_list = self.driver.find_element_by_xpath(".//*[@id='main-content']/main/section[" + str(a) + "]")
            self.assertTrue((cards_list).is_displayed())
            a += 1

    def test_3_run_on_startup(self):
        # check "Run LBRY automatically when I start my computer" is eneabled
        checkbox = self.driver.find_element_by_xpath(".//*[@id='main-content']/main/section[1]/label/input")
        self.assertTrue((checkbox).is_enabled())
        checkbox.click()
        self.assertTrue((checkbox).is_displayed())

    def test_4_download_directory(self):
        # find input and check value
        directory_select = self.driver.find_element_by_xpath(".//*[@id='main-content']/main/section[2]/input")
        self.assertIn("/home/developer/Downloads",
            directory_select.get_attribute("value"))

        # change value
        directory_select.click()
        directory_select.clear()
        directory_select.send_keys("/home/developer/Desktop")
        time.sleep(3)
        self.assertIn("/home/developer/Desktop",
            directory_select.get_attribute("value"))

        directory_select.click()
        directory_select.clear()
        directory_select.send_keys("/home/developer/Downloads")
        time.sleep(3)
        self.assertIn("/home/developer/Downloads",
            directory_select.get_attribute("value"))

    def test_5_bandwidth_limits_change_upload(self):
        max_upload_unlim = self.driver.find_element_by_xpath(".//*[@id='main-content']/main/section[3]/div[1]/label[1]/input")
        max_upload_limit = self.driver.find_element_by_xpath(".//*[@id='main-content']/main/section[3]/div[1]/label[2]/input")

        # check "max upload unlimited" and "max download unlimited" is selected
        self.assertTrue((max_upload_unlim).is_displayed())

        # change max upload
        max_upload_limit.click()
        max_upload_number_input = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                        ".//*[@id='main-content']/main/section[3]/div[1]/label[2]/span/input")))
        max_upload_number_input.click()
        max_upload_number_input.send_keys("1024")
        time.sleep(3)
        self.driver.refresh()
        self.assertIn("1024", self.driver.find_element_by_xpath(".//*[@id='main-content']/main/section[3]/div[1]/label[2]/span/input")
                      .get_attribute("value"))
        self.driver.find_element_by_xpath(".//*[@id='main-content']/main/section[3]/div[1]/label[1]/input").click()
        self.driver.refresh()
        self.driver.find_element_by_xpath(".//*[@id='main-content']/main/section[3]/div[1]/label[2]/input").click()
        self.assertIn("0", self.driver.find_element_by_xpath(".//*[@id='main-content']/main/section[3]/div[1]/label[2]/span/input")
                      .get_attribute("value"))

    def test_6_bandwidth_limit_change_download(self):
        # check and "max download unlimited" is selected
        max_download_unlim = self.driver.find_element_by_xpath(".//*[@id='main-content']/main/section[3]/div[2]/label[1]/input")
        max_download_limit = self.driver.find_element_by_xpath(".//*[@id='main-content']/main/section[3]/div[2]/label[2]/input")
        self.assertTrue((max_download_unlim).is_displayed())

        max_download_limit.click()
        max_download_number_input = wait.until(EC.element_to_be_clickable((
            By.XPATH, ".//*[@id='main-content']/main/section[3]/div[2]/label[2]/span/input")))
        max_download_number_input.click()
        max_download_number_input.send_keys("1024")
        time.sleep(2)
        self.driver.refresh()
        self.assertIn("1024", self.driver.find_element_by_xpath(".//*[@id='main-content']/main/section[3]/div[2]/label[2]/span/input")
                      .get_attribute("value"))
        self.driver.find_element_by_xpath(".//*[@id='main-content']/main/section[3]/div[2]/label[1]/input").click()
        self.driver.refresh()
        self.driver.find_element_by_xpath(".//*[@id='main-content']/main/section[3]/div[2]/label[2]/input").click()
        self.assertIn("0", self.driver.find_element_by_xpath(".//*[@id='main-content']/main/section[3]/div[2]/label[2]/span/input")
                      .get_attribute("value"))


    def test_7_show_nsfw_content(self):
        # check "show_nsfw_content" checkbox
        show_nsfw_content_checkbox = wait.until(EC.element_to_be_clickable((By.XPATH,
                                            ".//*[@id='main-content']/main/section[4]/div/label/input")))
        self.assertTrue((show_nsfw_content_checkbox).is_enabled())
        show_nsfw_content_checkbox.click()
        self.assertTrue((show_nsfw_content_checkbox).is_displayed())

    def test_8_share_diagnostic_data(self):
        # check "Help make LBRY better by contributing diagnostic data about my usage" checkbox
        help_checkbox = wait.until(EC.element_to_be_clickable((By.XPATH,
                                            ".//*[@id='main-content']/main/section[4]/div/label/input")))
        self.assertTrue((help_checkbox).is_enabled())
        help_checkbox.click()
        self.assertTrue((help_checkbox).is_displayed())


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    if __name__ == '__main__':
        unittest.main()