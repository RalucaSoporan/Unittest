import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class Login_page(unittest.TestCase):

    USERNAME = (By.XPATH, '//*[@name="username"]')
    PASSWORD = (By.XPATH, '//*[@name="password"]')
    LOGIN_BUTTON = (By.XPATH, '//*[@type="submit"]')
    LOGO_TITLE = (By.XPATH, '//*[@alt="company-branding"]')
    LOGIN_TITLE= (By.XPATH, '//h5')
    INVALID_CREDENTIALS = (By.XPATH, '//*[text() = "Invalid credentials"]')
    REQUIRED = (By.XPATH, '//span[text() = "Required"]')


    def setUp(self):
        '''It contains all the steps that must be taken before class test time'''
        self.chrome = webdriver.Chrome()
        self.chrome.implicitly_wait(10)
        self.chrome.maximize_window()
        self.chrome.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')


    def test_logo_page(self):
        '''I checked if the logo appears on the page'''
        title = self.chrome.find_element(*self.LOGO_TITLE)
        actual = title.is_displayed()
        self.assertTrue(actual, True)

    def test_text_page_title(self):
        '''I checked the page title'''
        title = self.chrome.find_element(*self.LOGIN_TITLE)
        expected = 'Login'
        actual = title.text
        self.assertEqual(expected,actual)


    def test_login_page_with_user_name_incorrect_and_password_correct(self):
        '''I checked if I can log in with an incorrect username and the correct password
        error displayed
        '''
        self.chrome.find_element(*self.USERNAME).send_keys('incorrect_username')
        self.chrome.find_element(*self.PASSWORD).send_keys('admin123')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        time.sleep(3)
        expected = 'Invalid credentials'
        actual = self.chrome.find_element(*self.INVALID_CREDENTIALS).text
        self.assertEqual(expected, actual)


    def test_login_page_with_user_name_correct_and_password_incorrect(self):
        '''I checked if I can log in with an correct username and the incorrect password,
         error displayed
         '''
        self.chrome.find_element(*self.USERNAME).send_keys('Admin')
        self.chrome.find_element(*self.PASSWORD).send_keys('password_invalid')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        expected = 'Invalid credentials'
        actual = self.chrome.find_element(*self.INVALID_CREDENTIALS).text
        self.assertEqual(expected, actual)

    def test_login_page_with_user_name_correct_and_password_none(self):
        '''I checked if I can log in with the correct username and missing password,
        error displayed
        '''
        self.chrome.find_element(*self.USERNAME).send_keys('Admin')
        self.chrome.find_element(*self.PASSWORD).send_keys('')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        list = self.chrome.find_elements(*self.REQUIRED)
        actual= list[0].text
        expected = 'Required'
        self.assertEqual(expected, actual)


    def test_login_page_with_user_name_none_and_password_none(self):
        '''I checked if I can log in with the missing username and correct password
        error displayed
        '''
        self.chrome.find_element(*self.USERNAME).send_keys('')
        self.chrome.find_element(*self.PASSWORD).send_keys('')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        list = self.chrome.find_elements(*self.REQUIRED)
        expected = 'Required'
        actual1 = list[0].text
        actual2 = list[1].text
        self.assertEqual(expected, actual1)
        self.assertEqual(expected,actual2)

    def test_error_disappears_when_I_put_credentials(self):
        '''check if the credentials error has disappeared'''
        self.chrome.find_element(*self.USERNAME).send_keys('')
        self.chrome.find_element(*self.PASSWORD).send_keys('')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        list = self.chrome.find_elements(By.XPATH, '//span[text() = "Required"]')
        self.chrome.find_element(*self.USERNAME).send_keys('invalid_name')
        self.chrome.find_element(*self.PASSWORD).send_keys('invalid_password')
        time.sleep(3)
        with self.assertRaises(NoSuchElementException):
            self.chrome.find_element(*self.REQUIRED)




    def test_login_page_with_user_name_correct_and_password_correct(self):
        '''I tried to log in with the correct credentials'''
        self.chrome.find_element(*self.USERNAME).send_keys('Admin')
        self.chrome.find_element(*self.PASSWORD).send_keys('admin123')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        expected = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        actual = self.chrome.current_url
        self.assertEqual(expected, actual)


    def tearDown(self):
        '''All the activities that must be performed after any test in the respective class'''
        self.chrome.quit()







