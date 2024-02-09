import random
import string

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects import LoginPage
from pageObjects.LoginPage import LoginPageClass
from pageObjects.RegistrationPage import RegistrationClass
from utilities.readconfig import Readconfig
from utilities.Logger import LogGenerator


# @pytest.mark.usefixtures("setup")
# class TestUserProfile:
#     def test_user_login_001(self,setup):
#         # open browser
#         driver = webdriver.Chrome()
#         driver.maximize_window()
#         # go to url
#         driver.get("https://automation.credence.in/login")
#         # this is fixture captured from conftest
#         self.driver = setup
#         self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys("Credencetest@test.com")
#         self.driver.find_element(By.CSS_SELECTOR, "input[id='password']").send_keys("Credence@123")
#         # click login
#         self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
#         try:
#             self.driver.find_element(By.XPATH, "//h2[normalize-space()='CredKart']")
#             print("Login TestCase passed")
#         except:
#             print("Login TestCase failed")
#
#     # user registration in normal way
#     def test_user_registration_001(self, setup):
#         # open browser
#         driver = webdriver.Chrome()
#          driver.maximize_window()
#         self.driver = driver
#         self.driver.get("https://automation.credence.in/register")
#         self.driver.find_element(By.ID,"name").send_keys("Credence")
#         self.driver.find_element(By.ID,"email").send_keys("Credence_tpest@test003.com")
#         self.driver.find_element(By.NAME,"password").send_keys("Credence@123")
#         self.driver.find_element(By.NAME,"password_confirmation").send_keys("Credence@123")
#         self.driver.find_element(By.CLASS_NAME,"btn").click()
#         # a = driver.find_element(By.XPATH, "//h2[normalize-space()='CredKart']").text
#         try:
#             a = self.driver.find_element(By.XPATH, "//h2[normalize-space()='CredKart']").text
#             print("Registration TestCase is Passed")
#         except:
#             print("Registration TestCase is Failed")


# #  same code like above but using LoginPage pageobject and RegistrationPage pageobject
@pytest.mark.usefixtures("setup")
class TestUserProfiles:
    user_email = Readconfig.get_user_email() # this from utilities to get common data :Credencetest@test.com
    Password = Readconfig.get_password()
    log = LogGenerator.logg_in()
    def test_user_login_001(self,setup):
        # # open browser
        # driver = webdriver.Chrome()
        # driver.maximize_window()
        # driver.get("https://automation.credence.in/login")
        self.log.info("Testcase test_user_login_001 is stared")
        self.log.info("Opening browser")
        self.driver = setup
        # imported page object
        self.lp = LoginPageClass(self.driver)
        # self.lp.enter_username("Credencetest@test.com") # this hardcode value change with below code
        self.lp.enter_username(self.user_email) # this take data from readconfig file and readconfig read data from config.ini
        self.log.info("Entering username")
        # self.lp.enter_password("Credence@123")  # this hardcode value change with below code
        self.lp.enter_password(self.Password)  # this take data from readconfig file and readconfig read data from config.ini
        self.log.info("Entering password")
        # click login button
        self.lp.click_login_button()
        self.log.info("Click on login button")

        if self.lp.validate_status() == "TestCase is passed":
            self.log.info("Testcase:test_user_login_001 is passed")
            self.driver.save_screenshot("..\\Screenshots\\test_user_login_001_Pass.png")
            assert True
        else:
            self.log.info("Testcase:test_user_login_001 is failed")
            self.driver.save_screenshot("..\\Screenshots\\test_user_login_001_Fail.png")
            assert False
        self.log.info("Testcase:test_user_login_001 is passed")

    def test_user_registration_001(self, setup):
        # driver = webdriver.Chrome()
        # driver.maximize_window()
        self.driver = setup
        self.rp = RegistrationClass(self.driver)
        self.driver.get("https://automation.credence.in/register")
        self.rp.enter_name("Credence")
        # enter email
        email = generate_email()
        self.rp.enter_email(email)
        print(email)
        # enter password
        self.rp.enter_password("Credence@123")
        # enter confirm password
        self.rp.enter_ConfirmPassword("Credence@123")
        # click register button
        self.rp.Click_RegisterButton()
        # varify registration status
        self.lp = LoginPageClass(self.driver)
        if self.lp.validate_status() == "TestCase is passed":
            self.driver.save_screenshot("..\\Screenshots\\User_registration002_pass.png")
            assert True
        else:
            self.driver.save_screenshot("..\\Screenshots\\test_UserRegistration002_fail.png")
            assert False

def generate_email():
    username = ''.join(random.choices(string.ascii_lowercase,k=5))
    domain = random.choice(['gmail.com', 'ymail.com', 'outlook.com'])
    return f"{username}@{domain}"
