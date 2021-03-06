import os
import unittest
from appium import webdriver
from time import sleep
from lib2to3.fixer_util import String

#appium -p 4492 -bp 2251 -U 434aab08
#appium -p 4493 -bp 2252 -U 93e2da8b

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class ContactsAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.0.2'
        desired_caps['deviceName'] = 'Xiaomi2S'
        desired_caps['udid'] = '434aab08'
        #desired_caps['app'] = PATH(
        #    '../../../sample-code/apps/ContactManager/ContactManager.apk'
        #)
        desired_caps['appPackage'] = 'com.starhub.rcsstarhubstaging'
        desired_caps['appActivity'] = 'com.starhub.rcsstarhubstaging.login.LoginSlapshActivity'
        #if would like to input Chinese,but appium input method has a bug
#         desired_caps["unicodeKeyboard"] = "True"
#         desired_caps["resetKeyboard"] = "True"

        self.driver = webdriver.Remote('http://localhost:4492/wd/hub', desired_caps)
        
        sleep(5)  #if too short, will report error

    def tearDown(self):
        self.driver.quit()

    def test_add_contacts(self):
        #         accessibility_id=content-desc
        contacts_btn = self.driver.find_element_by_id("com.starhub.rcsstarhubstaging:id/radio_button_contacts")
        contacts_btn.click()
        
        #in Contacts Screen
        String_0 = self.driver.current_activity
        print(String_0) #'com.starhub.messageplus.ui.MainActivity'
        all_bar = self.driver.find_element_by_name("All")
        all_bar.click()
        
        

#         textfields = self.driver.find_elements_by_class_name("android.widget.EditText")
#         textfields[0].send_keys("Appium User")
#         textfields[2].send_keys("someone@appium.io")
# 
#         self.assertEqual('Appium User', textfields[0].text)
#         self.assertEqual('someone@appium.io', textfields[2].text)
# 
#         self.driver.find_element_by_accessibility_id("Save").click()

        # for some reason "save" breaks things
#         alert = self.driver.switch_to_alert()

        # no way to handle alerts in Android
#         self.driver.find_element_by_android_uiautomator('new UiSelector().clickable(true)').click()
# 
#         self.driver.press_keycode(3)



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ContactsAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)