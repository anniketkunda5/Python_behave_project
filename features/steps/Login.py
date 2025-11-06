import time
from datetime import datetime
from behave import *
from features.pages.HomePage import HomePage
from features.pages.AccountPage import AccountPage
from features.pages.LoginPage import LoginPage
from utilities import Email_With_Timestamp_Generator


@given(u'I navigated to the login page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.click_on_my_account()
    context.login_page=context.home_page.select_login_option()

@when(u'I enter valid email address as "{email}" and valid password as "{password}" into the fields')
def step_impl(context,email,password):
    context.login_page.enter_email_address(email)
    context.login_page.enter_password(password)

@when(u'click on login button')
def step_impl(context):
    context.account_page=context.login_page.click_on_login_button()

@then(u'I should got logged in')
def step_impl(context):
    assert context.account_page.display_status_of_edit_your_account_info_page()

@when(u'I enter valid email address as "{email}" and invalid password as "{password}" into the fields')
def step_impl(context,email,password):
    invalid_password=Email_With_Timestamp_Generator.get_password_with_timestamp()
    context.login_page.enter_email_address(email)
    context.login_page.enter_password(invalid_password)

@then(u'I should get proper warning message')
def step_impl(context):
    time.sleep(1)
    assert context.login_page.login_warning_message('Warning: No match for E-Mail Address and/or Password.')

@when(u'I enter invalid email and invalid password into the fields')
def step_impl(context):
    time_stamp = datetime.now().strftime("%Y%m%d%I:%M:%S%p")
    invalid_password = "pwd" + time_stamp
    invalid_email = "mail" + time_stamp + "@gmail.com"
    #context.login_page = LoginPage(context.driver)
    context.login_page.enter_email_address(invalid_email)
    context.login_page.enter_password(invalid_password)


@when(u'I do not enter anything into login and password fields')
def step_impl(context):
    context.login_page.enter_email_address("")
    context.login_page.enter_password("")
