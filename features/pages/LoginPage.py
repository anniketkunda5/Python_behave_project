from selenium.webdriver.common.by import By

from features.pages.AccountPage import AccountPage
from features.pages.BasePage import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    email_address_field_id = "input-email"
    password_field_id = "input-password"
    login_button_xpath = "//input[@type='submit']"
    login_warning_message_xpath = "//div[@class='alert alert-danger alert-dismissible']"

    def enter_email_address(self,email_text):
        self.type_into_element("email_address_field_id",self.email_address_field_id,email_text)
        #self.driver.find_element(By.ID,self.email_address_field_id).send_keys(email_text)

    def enter_password(self,password_text):
        self.type_into_element("password_field_id",self.password_field_id,password_text)
        #self.driver.find_element(By.ID,self.password_field_id).send_keys(password_text)

    def click_on_login_button(self):
        self.click_on_element("login_button_xpath",self.login_button_xpath)
        #self.driver.find_element(By.XPATH,self.login_button_xpath).click()
        return AccountPage(self.driver)

    def login_warning_message(self,Warn_msg):
        return self.retrive_element_text_should_contains("login_warning_message_xpath",self.login_warning_message_xpath,Warn_msg)
        #return self.driver.find_element(By.XPATH,self.login_warning_message_xpath).text.__contains__(Warn_msg)

