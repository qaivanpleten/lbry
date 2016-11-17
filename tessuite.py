import unittest
from check_discover_page import check_discover_page
from settings_page import check_settings_page
from help_page import check_help_page
from my_wallet_page import check_wallet_page


# get all tests
discoverpage_test = unittest.TestLoader().loadTestsFromTestCase(check_discover_page)
settingpage_test = unittest.TestLoader().loadTestsFromTestCase(check_settings_page)
helppage_test = unittest.TestLoader().loadTestsFromTestCase(check_help_page)
walletpage_test = unittest.TestLoader().loadTestsFromTestCase(check_wallet_page)

smoke_tests = unittest.TestSuite((discoverpage_test, settingpage_test, helppage_test, walletpage_test))

# run the suite
a = unittest.TextTestRunner(verbosity=2).run(smoke_tests)
#xmlrunner.XMLTestRunner(verbosity=2, output='test-reports').run(smoke_tests)