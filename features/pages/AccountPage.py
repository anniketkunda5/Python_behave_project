from selenium.webdriver.common.by import By


class AccountPage:
    def __init__(self, driver):
        self.driver = driver

    edit_your_account_info_option_link_text = "Edit your account information"
    account_create_success_message_XPATH = "//div[@id='common-success']//div[@id='content']"

    def display_status_of_edit_your_account_info_page(self):
        return self.driver.find_element(By.LINK_TEXT,self.edit_your_account_info_option_link_text).is_displayed()

    def account_create_success(self,Success_Message):
        return self.driver.find_element(By.XPATH,self.account_create_success_message_XPATH).text.__contains__(Success_Message)