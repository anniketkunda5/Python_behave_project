from selenium.webdriver.common.by import By
from features.pages.BasePage import BasePage


class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    valid_product_linktext = "HP LP3065"
    product_not_match_message_XPATH = "//input[@type='button']/following-sibling::p"

    def display_status_of_product(self):
        return self.display_status("valid_product_link_text",self.valid_product_linktext)
        #return self.driver.find_element(By.LINK_TEXT,self.valid_product_linktext).is_displayed()

    def product_not_match_message(self,expected_text):
        return self.retrive_element_text_should_equals("product_not_match_message_XPATH",self.product_not_match_message_XPATH,expected_text)
        #return self.driver.find_element(By.XPATH,self.product_not_match_message_XPATH).text.__eq__(expected_text)