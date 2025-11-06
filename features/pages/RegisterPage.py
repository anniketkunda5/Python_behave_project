import time

from selenium.webdriver.common.by import By

from features.pages.AccountPage import AccountPage
from features.pages.BasePage import BasePage


class Register_Page(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    register_first_name_ID = "input-firstname"
    register_last_name_ID = "input-lastname"
    register_email_ID = "input-email"
    register_telephone_ID = "input-telephone"
    register_password_ID = "input-password"
    register_confirm_ID = "input-confirm"
    register_terms_XPATH = "//input[@type='checkbox']"
    register_continue_button_XPATH = "//input[@type='submit']"
    register_email_warning_XPATH = "//div[@class='alert alert-danger alert-dismissible']"
    privacy_policy_warning_XPATH = "//div[@class='alert alert-danger alert-dismissible']"
    firstname_warning_XPATH = "//input[@name='firstname']/following-sibling::div"
    lastname_warning_XPATH = "//input[@name='lastname']/following-sibling::div"
    email_warning_XPATH = "//input[@name='email']/following-sibling::div"
    telephone_warning_XPATH= "//input[@name='telephone']/following-sibling::div"
    password_warning_XPATH= "//input[@name='password']/following-sibling::div"

    def register_first_name(self,first_name):
        self.type_into_element("register_first_name_ID",self.register_first_name_ID,first_name)
        #self.driver.find_element(By.ID,self.register_first_name_ID).send_keys(first_name)

    def register_last_name(self,last_name):
        self.type_into_element("register_last_name_ID",self.register_last_name_ID,last_name)
        #self.driver.find_element(By.ID,self.register_last_name_ID).send_keys(last_name)

    def register_email(self,email):
        self.type_into_element("register_email_ID",self.register_email_ID,email)
        #self.driver.find_element(By.ID,self.register_email_ID).send_keys(email)

    def register_telephone(self,telephone):
        self.type_into_element("register_telephone_ID",self.register_telephone_ID,telephone)
        #self.driver.find_element(By.ID,self.register_telephone_ID).send_keys(telephone)

    def register_password(self,password):
        self.type_into_element("register_password_ID",self.register_password_ID,password)
        #self.driver.find_element(By.ID,self.register_password_ID).send_keys(password)

    def register_password_confirm(self,confirm):
        self.type_into_element("register_confirm_ID",self.register_confirm_ID,confirm)
        #self.driver.find_element(By.ID,self.register_confirm_ID).send_keys(confirm)

    def register_terms_submit(self):
        self.click_on_element("register_terms_XPATH",self.register_terms_XPATH)
        #self.driver.find_element(By.XPATH,self.register_terms_XPATH).click()

    def register_continue_button(self):
        self.click_on_element("register_continue_button_XPATH",self.register_continue_button_XPATH)
        #self.driver.find_element(By.XPATH,self.register_continue_button_XPATH).click()
        return AccountPage(self.driver)

    def register_email_warning(self,Warning_msg):
        return self.retrive_element_text_should_contains("register_email_warning_XPATH",self.register_email_warning_XPATH,Warning_msg)
        #return self.driver.find_element(By.XPATH,self.register_email_warning_XPATH).text.__contains__(Warning_msg)
    def display_status_of_all_warning_messages(self,expected_privacy_policy_warning,expected_firstname_warning,expected_lastname_warning,expected_email_warning,expected_telephone_warning,expected_password_warning):
        privacy_status= self.retrive_element_text_should_contains("privacy_policy_warning_XPATH",self.privacy_policy_warning_XPATH,expected_privacy_policy_warning)
        #privacy_status=self.driver.find_element(By.XPATH,self.privacy_policy_warning_XPATH).text.__contains__(expected_privacy_policy_warning)
        firstname_status = self.retrive_element_text_should_equals("firstname_warning_XPATH",self.firstname_warning_XPATH,expected_firstname_warning)
        #firstname_status=self.driver.find_element(By.XPATH,self.firstname_warning_XPATH).text.__eq__(expected_firstname_warning)
        lastname_status = self.retrive_element_text_should_equals("lastname_warning_XPATH",self.lastname_warning_XPATH,expected_lastname_warning)
        #lastname_status=self.driver.find_element(By.XPATH,self.lastname_warning_XPATH).text.__eq__(expected_lastname_warning)
        email_status = self.retrive_element_text_should_equals("email_warning_XPATH",self.email_warning_XPATH,expected_email_warning)
        #email_status=self.driver.find_element(By.XPATH,self.email_warning_XPATH).text.__eq__(expected_email_warning)
        telephone_status = self.retrive_element_text_should_equals("telephone_warning_XPATH",self.telephone_warning_XPATH,expected_telephone_warning)
        #telephone_status=self.driver.find_element(By.XPATH,self.telephone_warning_XPATH).text.__eq__(expected_telephone_warning)
        password_status = self.retrive_element_text_should_equals("password_warning_XPATH",self.password_warning_XPATH,expected_password_warning)
        #password_status=self.driver.find_element(By.XPATH,self.password_warning_XPATH).text.__eq__(expected_password_warning)
        return self.return_and_status(privacy_status, firstname_status, lastname_status, email_status, telephone_status, password_status)
