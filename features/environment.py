import allure
from allure_behave.utils import step_status
from allure_commons.types import AttachmentType
from selenium import webdriver
from utilities import ConfigReader

def before_scenario(context,driver):
    browser_name = ConfigReader.read_configuration("basic info","browser").lower()
    if browser_name == "chrome":
        context.driver = webdriver.Chrome()
    if browser_name.__eq__("firefox"):
        context.driver = webdriver.Firefox()
    if browser_name.__eq__("edge"):
        context.driver = webdriver.Edge()
    context.driver.maximize_window()
    context.driver.get(ConfigReader.read_configuration("basic info","url"))

    context.driver.refresh()

def after_scenario(context,driver):
    context.driver.quit()

def after_step(context,step):
    if step.status=='failed':
        allure.attach(context.driver.get_screenshot_as_png(),
                      name="failed_screenshot",
                      attachment_type=AttachmentType.PNG)