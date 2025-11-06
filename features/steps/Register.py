import time
from datetime import datetime
from behave import *
from features.pages.AccountPage import AccountPage
from features.pages.HomePage import HomePage
from features.pages.RegisterPage import Register_Page


@given(u'I navigate to register page')
def step_impl(context):
    context.home_page=HomePage(context.driver)
    context.home_page.click_on_my_account()
    context.register_page=context.home_page.select_register_option()

@when(u'I enter below details in the mandatory fields')
def step_impl(context):
    for row in context.table:
        context.register_page=Register_Page(context.driver)
        context.register_page.register_first_name(row['first_name'])
        context.register_page.register_last_name(row['last_name'])
        time_stamp = datetime.now().strftime("%Y%m%d%I%M%S%p")
        Gmail_id = "man"+time_stamp+"@gmail.com"
        context.register_page.register_email(Gmail_id)
        context.register_page.register_telephone(row['telephone'])
        context.register_page.register_password(row['password'])
        context.register_page.register_password_confirm(row['password'])
        context.register_page.register_terms_submit()

@when(u'I click on Continue button')
def step_impl(context):
    context.account_page=context.register_page.register_continue_button()

@then(u'Account should get created')
def step_impl(context):
    Success_Message = "Congratulations! Your new account has been successfully created!"
    assert context.account_page.account_create_success(Success_Message)

@when(u'I enter details into all fields')
def step_impl(context):
    for row in context.table:
        context.register_page.register_first_name(row['first_name'])
        context.register_page.register_last_name(row['last_name'])
        time_stamp = datetime.now().strftime("%Y%m%d%I%M%S%p")
        Gmail_id = "man" + time_stamp + "@gmail.com"
        context.register_page.register_email(Gmail_id)
        context.register_page.register_telephone(row['telephone'])
        context.register_page.register_password(row['password'])
        context.register_page.register_password_confirm(row['password'])
        context.register_page.register_terms_submit()

@when(u'I enter details into all fields except email field')
def step_impl(context):
    for row in context.table:
        context.register_page.register_first_name(row['first_name'])
        context.register_page.register_last_name(row['last_name'])
        context.register_page.register_email("")
        context.register_page.register_telephone(row['telephone'])
        context.register_page.register_password(row['password'])
        context.register_page.register_password_confirm(row['password'])
        context.register_page.register_terms_submit()
        context.register_page.register_continue_button()

@when(u'I enter existing account mail into email field')
def step_impl(context):
    context.register_page.register_email("a.kunda@gmail.com")

@then(u'Proper warning message informing about duplicate account should be displayed')
def step_impl(context):
    Warning_msg= "Warning: E-Mail Address is already registered!"
    assert context.register_page.register_email_warning(Warning_msg)


@when(u'I dont enter anything into fields')
def step_impl(context):
    context.register_page = Register_Page(context.driver)
    context.register_page.register_first_name("")
    context.register_page.register_last_name("")
    context.register_page.register_email("")
    context.register_page.register_telephone("")
    context.register_page.register_password("")
    context.register_page.register_password_confirm("")
    #context.register_page.register_terms_submit()
    context.register_page.register_continue_button()

@then(u'Proper warning message for every mandatory fields should be displayed')
def step_impl(context):
    time.sleep(2)
    expected_privacy_policy_warning = "Warning: You must agree to the Privacy Policy!"
    expected_firstname_warning = "First Name must be between 1 and 32 characters!"
    expected_lastname_warning = "Last Name must be between 1 and 32 characters!"
    expected_email_warning = "E-Mail Address does not appear to be valid!"
    expected_telephone_warning = "Telephone must be between 3 and 32 characters!"
    expected_password_warning = "Password must be between 4 and 20 characters!"
    assert context.register_page.display_status_of_all_warning_messages(expected_privacy_policy_warning,
                                                                        expected_firstname_warning,
                                                                        expected_lastname_warning,
                                                                        expected_email_warning,
                                                                        expected_telephone_warning,
                                                                        expected_password_warning)
