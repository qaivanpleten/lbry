# import unittest, time,re
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import Select
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import NoAlertPresentException
# from faker import Faker
# f = Faker()
#
#
# class publish_file(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         cls.driver = webdriver.Chrome()
#         cls.driver.implicitly_wait(10)
#         cls.driver.maximize_window()
#         cls.driver.title
#         cls.driver.get("http://localhost:5279/")
#         global wait
#         wait = WebDriverWait(cls.driver, 15)
#
#
#     def test_1_go_to_pubish_page(self):
#         # find "publish" button and click
#         wait.until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='drawer']/a[2]"))).click()
#         # check url
#         self.assertIn("http://localhost:5279/?publish", self.driver.current_url)
#         # check header title
#         self.assertIn("Publish",
#                       self.driver.find_element_by_xpath(".//*[@id='header']/div/h1")
#                       .get_attribute("textContent"))
#
#
#     def test_2_check_page_content(self):
#         # check cards
#         a = 1
#         while a < 6:
#             cards_list = self.driver.find_element_by_xpath(".//*[@id='main-content']/main/form/section[" + str(a) + "]")
#             self.assertTrue((cards_list).is_displayed())
#             a += 1
#
#         # check "LBRY Name"
#         self.assertIn("LBRY Name",
#                       self.driver.find_element_by_xpath(".//*[@id='main-content']/main/form/section[1]/h4").
#                       get_attribute("textContent"))
#
#         # check "Choose File"
#         self.assertIn("Choose File",
#                       self.driver.find_element_by_xpath(".//*[@id='main-content']/main/form/section[2]/h4").
#                       get_attribute("textContent"))
#
#
#         # check "Bid Amount"
#         self.assertIn("Bid Amount",
#                       self.driver.find_element_by_xpath(".//*[@id='main-content']/main/form/section[3]/h4").
#                       get_attribute("textContent"))
#
#         # check "Fee"
#         self.assertIn("Fee",
#                       self.driver.find_element_by_xpath(".//*[@id='main-content']/main/form/section[4]/h4").
#                       get_attribute("textContent"))
#
#         # check "Additional Content Information (Optional)"
#         self.assertIn("Additional Content Information (Optional)",
#                       self.driver.find_element_by_xpath(".//*[@id='main-content']/main/form/section[6]/h4").
#                       get_attribute("textContent"))
#
#
#     def test_4_upload_file_complete(self):
#         global lbry_name
#         wait.until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='drawer']/a[2]"))).click()
#
#         # find "lbry name" input
#         lbry_name = f.name()
#         lbry_name = lbry_name.split(" ")
#         lbry_name = (lbry_name[0]).lower()
#         lbry_name_input = self.driver.find_element_by_xpath(
#             ".//*[@id='main-content']/main/form/section[1]/div/span/input")
#         lbry_name_input.clear()
#         lbry_name_input.send_keys(lbry_name)
#         time.sleep(3)
#         self.assertIn(lbry_name, self.driver.find_element_by_xpath(
#             ".//*[@id='main-content']/main/form/section[1]/div/em/strong").get_attribute("textContent"))
#
#         # choose file
#         file_input = self.driver.find_element_by_xpath(".//*[@id='main-content']/main/form/section[2]/span/input")
#         # file_input.clear()
#         file_input.send_keys("/home/developer/Изображения/tumblr_of8n6x25FT1r2qr2so1_500.jpg")
#         self.assertIn("File ready for publishing!",
#                       self.driver.find_element_by_xpath(".//*[@id='main-content']/main/form/section[2]/div")
#                       .get_attribute("textContent"))
#
#         # choose bid amount
#         bid_value = "0"
#         bid_amount_input = self.driver.find_element_by_xpath(
#             ".//*[@id='main-content']/main/form/section[3]/div/span/input")
#         bid_amount_input.clear()
#         bid_amount_input.send_keys(bid_value)
#         self.assertIn(bid_value, bid_amount_input.get_attribute("value"))
#
#         # choose fee - no fee
#         self.assertTrue((self.driver.find_element_by_xpath(
#             ".//*[@id='main-content']/main/form/section[4]/div/label[1]/span/input"))
#                         .is_enabled())
#
#         # fill "Your Content" form
#         title_input = self.driver.find_element_by_xpath(
#             ".//*[@id='main-content']/main/form/section[5]/div[1]/span/input")
#         author_input = self.driver.find_element_by_xpath(
#             ".//*[@id='main-content']/main/form/section[5]/div[2]/span/input")
#         license_select = Select(self.driver.find_element_by_xpath(
#             ".//*[@id='main-content']/main/form/section[5]/div[3]/span[1]/select"))
#         language_select = Select(
#             self.driver.find_element_by_xpath(".//*[@id='main-content']/main/form/section[5]/div[4]/span/select"))
#         description_textarea = self.driver.find_element_by_xpath(
#             ".//*[@id='main-content']/main/form/section[5]/div[5]/span/textarea")
#         nsfw_checkbox = self.driver.find_element_by_xpath(
#             ".//*[@id='main-content']/main/form/section[5]/div[6]/label/span/input")
#
#         title_input.clear()
#         title_input.send_keys(lbry_name)
#
#         author_input.clear()
#         author_input.send_keys(f.name())
#
#         self.assertEqual("Creative Commons Attribution 4.0 International",
#                          license_select.first_selected_option.text)
#         self.assertEqual("English", language_select.first_selected_option.text)
#
#         description_textarea.clear()
#         description_textarea.send_keys(f.text())
#
#         publish_button = self.driver.find_element_by_xpath(".//*[@id='main-content']/main/form/div/a[1]")
#         publish_button.click()
#         # check popup
#         self.assertTrue(self.driver.find_element_by_xpath("html/body/div[2]/div/div").is_displayed())
#         # confirm popup
#         self.driver.find_element_by_xpath("html/body/div[2]/div/div/div/a").click()
#
#
#     def test_5_check_uploaded_file(self):
#         # go to "published" page
#         self.driver.find_element_by_xpath(".//*[@id='drawer']/a[3]").click()
#         self.driver.find_element_by_xpath(".//*[@id='header']/nav/a[2]").click()