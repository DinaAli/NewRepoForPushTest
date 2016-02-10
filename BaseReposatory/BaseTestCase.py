import unittest
from selenium import webdriver

class BaseTestCase(unittest.TestCase):

    ''' parent class for all testcases
    all common functions for testcases should be written here
    '''
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    #def tearDown(self):
        #self.driver.quit()