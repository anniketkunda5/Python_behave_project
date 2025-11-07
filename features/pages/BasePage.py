from selenium.common import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def get_element(self,locator_type,locator_value ):
        element = None
        if locator_type.endswith("_id"):
            element = self.driver.find_element(By.ID, locator_value)
        elif locator_type.endswith("_ID"):
            element = self.driver.find_element(By.ID, locator_value)
        elif locator_type.endswith("_name"):
            element = self.driver.find_element(By.NAME, locator_value)
        elif locator_type.endswith("_class_name"):
            element = self.driver.find_element(By.CLASS_NAME, locator_value)
        elif locator_type.endswith("_link_text"):
            element = self.driver.find_element(By.LINK_TEXT, locator_value)
        elif locator_type.endswith("_xpath"):
            element = self.driver.find_element(By.XPATH, locator_value)
        elif locator_type.endswith("_XPATH"):
            element = self.driver.find_element(By.XPATH, locator_value)
        elif locator_type.endswith("_css"):
            element = self.driver.find_element(By.CSS_SELECTOR, locator_value)
        return element

    def click_on_element(self, locator_type, locator_value, timeout=10):
        try:
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(
                EC.element_to_be_clickable((self._get_by(locator_type), locator_value))
            )
            element.click()
        except TimeoutException:
            print(f"[ERROR] Timeout: Element not clickable -> {locator_value}")
            raise
        except ElementClickInterceptedException:
            print(f"[WARNING] Click intercepted, retrying via JavaScript -> {locator_value}")
            self.driver.execute_script("arguments[0].click();", element)

    def _get_by(self, locator_type):
        if locator_type.endswith("_id") or locator_type.endswith("_ID"):
            return By.ID
        elif locator_type.endswith("_name"):
            return By.NAME
        elif locator_type.endswith("_class_name"):
            return By.CLASS_NAME
        elif locator_type.endswith("_link_text"):
            return By.LINK_TEXT
        elif locator_type.endswith("_xpath") or locator_type.endswith("_XPATH"):
            return By.XPATH
        elif locator_type.endswith("_css"):
            return By.CSS_SELECTOR
        else:
            raise ValueError(f"Invalid locator type: {locator_type}")


    def verify_page_title(self, expected_title):
        return self.driver.title == expected_title

    def type_into_element(self, locator_type, locator_value, text_to_entered):
        element = self.get_element(locator_type, locator_value)
        element.click()
        element.clear()
        element.send_keys(text_to_entered)
    def retrive_element_text_should_contains(self,locator_type,locator_value,expected_text):
        element = self.get_element(locator_type,locator_value)
        return element.text.__contains__(expected_text)

    def retrive_element_text_should_equals(self, locator_type, locator_value, expected_text):
        element = self.get_element(locator_type, locator_value)
        return element.text.__eq__(expected_text)
    def return_and_status(self,privacy_status,firstname_status,lastname_status,email_status,telephone_status,password_status):
        if privacy_status and firstname_status and lastname_status and email_status and telephone_status and password_status:
            return True
        else:
            return False
    def display_status(self,locator_type, locator_value):
        element = self.get_element(locator_type, locator_value)
        # if element:
        #     return element.is_displayed()
        # else:
        #     print(f"[WARNING] Element not found for display check: {locator_value}")
        #     return False
        #return element.is_displayed()
        if element:
            return element.is_displayed()
        else:
            print(f"[WARNING] Element not found for locator: {locator_type} = {locator_value}")
            return False

