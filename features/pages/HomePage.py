from selenium.webdriver.common.by import By

from features.pages.BasePage import BasePage
from features.pages.LoginPage import LoginPage
from features.pages.RegisterPage import Register_Page
from features.pages.SearchPage import SearchPage

search_box_name = "search"
search_box_button_XPATH = "//span/button[@type='button']"

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    my_account_option_xpath= "//span[text()='My Account']"
    login_option_link_text = "Login"
    register_option_link_text = "Register"
    def click_on_my_account(self):
        self.click_on_element("my_account_option_xpath", self.my_account_option_xpath)
        # self.driver.find_element(By.XPATH,self.my_account_option_xpath).click()

    def select_login_option(self):
        self.click_on_element("login_option_link_text", self.login_option_link_text)
        #self.driver.find_element(By.LINK_TEXT,self.login_option_link_text).click()
        return LoginPage(self.driver)

    def select_register_option(self):
        self.click_on_element("register_option_link_text", self.register_option_link_text)
        #self.driver.find_element(By.LINK_TEXT,self.register_option_link_text).click()
        return Register_Page(self.driver)

    def check_homepage_title(self,expected_title):
        return self.verify_page_title(expected_title)
        #return self.driver.title == expected_title

    def enter_product_into_search_box_field(self,product_text):
        self.type_into_element("search_box_name", search_box_name, product_text)
        #self.driver.find_element(By.NAME,search_box_name).send_keys(product_text)

    def click_search_button(self):
        self.click_on_element("search_box_button_XPATH",search_box_button_XPATH)
        #self.driver.find_element(By.XPATH,search_box_button_XPATH).click()
        return SearchPage(self.driver)




