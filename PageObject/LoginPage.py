from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    '''
    class contain all webselemnts of page and functions for interactiong with elements
    '''
    #Locators
    usernameBox = (By.ID,'cred_userid_inputtext')
    continue_Button = (By.ID,'cred_continue_button')
    account_title = (By.CLASS_NAME,'aad_account_tile')
    password_txt = (By.ID,'cred_password_inputtext')
    signin_button = (By.ID,'cred_sign_in_button')
    my_first_project = (By.CLASS_NAME,'icon-container')
    welcome = (By.ID,'Welcome')

    def sign_in(self,username,password):
        self.driver.find_element(*LoginPage.usernameBox).send_keys(username)
        self.driver.find_element(*LoginPage.continue_Button).click()
        self.driver.find_element(*LoginPage.account_title).click()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id('cred_password_inputtext').send_keys(password)
        self.driver.find_element(*LoginPage.signin_button).click()
        self.driver.implicitly_wait(30)
        self.driver.find_element(*LoginPage.my_first_project).click()
        self.driver.find_element(*LoginPage.welcome).click()