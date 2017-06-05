import os
import unittest
from appium import webdriver
# from time import sleep
import time

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class ContactsAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.0'
        # desired_caps['deviceName'] = '434aab08'  # xiaomi 2S, 5.0.2
        desired_caps['deviceName'] = '416124ea'   # OnePlus A3000, 7.0
        # desired_caps['app'] = PATH(
        #     ''
        # )
        desired_caps['appPackage'] = 'com.globalroam.pfingo.staging'
        desired_caps['appActivity'] = 'com.globalroam.pfingo.ui.WelcomeActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(7)

    def tearDown(self):
        self.driver.quit()

    def test_add_contacts(self):
        el1 = self.driver.find_element_by_id('com.globalroam.pfingo.staging:id/edit_number')
        el1.click()
        time.sleep(1)
        el1.send_keys('13551856640')
        print(self.driver.current_activity)

        el2 = self.driver.find_element_by_id('com.globalroam.pfingo.staging:id/country_code')
        self.assertEqual(el2.text, '+86')
        time.sleep(1)
        el2.click()
        time.sleep(1)

        el3 = self.driver.find_element_by_id('com.globalroam.pfingo.staging:id/read_checkBox')
        el3.click()

        el4 = self.driver.find_element_by_id('com.globalroam.pfingo.staging:id/active_service')
        el4.click()
        time.sleep(10)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ContactsAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)