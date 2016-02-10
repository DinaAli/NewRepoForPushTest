import unittest
from selenium import webdriver
from PageObject.LoginPage import LoginPage
from BaseReposatory.BaseTestCase import BaseTestCase

class MyTestCase(BaseTestCase):

    def test_Login_valid_credintials(self):
        driver = self.driver
        driver.get("https://sneakypython.visualstudio.com")
        LoginPage.sign_in(self,"dali@integrant.com","Cowa0589")

if __name__ == '__main__':
    unittest.main()
