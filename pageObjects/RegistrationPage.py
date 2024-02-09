from selenium import webdriver
from selenium.webdriver.common.by import By

class RegistrationClass:
    Text_Name_ID = "name"
    Text_Email_ID = "email"
    Text_Password_Name = "password"
    Text_ConfirmPassword_Name = "password_confirmation"
    Click_Register_Button_ClassName = "btn"
    Validate_Status_Xpath = "//h2[normalize-space()='CredKart']"

    def __init__(self,driver):
        self.driver = driver

    def enter_name(self,name):
        self.driver.find_element(By.ID,self.Text_Name_ID).send_keys(name)

    def enter_email(self, email):
        self.driver.find_element(By.ID, self.Text_Email_ID).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(By.NAME, self.Text_Password_Name).send_keys(password)

    def enter_ConfirmPassword(self, confirm_password):
        self.driver.find_element(By.NAME, self.Text_ConfirmPassword_Name).send_keys(confirm_password)

    def Click_RegisterButton(self):
        self.driver.find_element(By.CLASS_NAME, self.Click_Register_Button_ClassName).click()



