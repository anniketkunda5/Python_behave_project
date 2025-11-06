from behave import *
from features.pages.HomePage import HomePage

@given(u'I got navigate to home page')
def step_impl(context):
    expected_title= "Your Store"
    context.home_page = HomePage(context.driver)
    assert context.home_page.check_homepage_title(expected_title)

@when(u'I enter valid product say "{product}" into the search box field')
def step_impl(context,product):
    context.home_page.enter_product_into_search_box_field(product)

@when(u'I click on Search button')
def step_impl(context):
    context.search_page=context.home_page.click_search_button()

@then(u'Valid product should get displayed in search results')
def step_impl(context):
    assert context.search_page.display_status_of_product()

@when(u'I enter invalid product say "{product}" into the search box field')
def step_impl(context,product):
    context.home_page.enter_product_into_search_box_field(product)

@then(u'Proper message should be displayed in search result')
def step_impl(context):
    assert context.search_page.product_not_match_message("There is no product that matches the search criteria.")

@when(u'I dont enter anything into search box field')
def step_impl(context):
    context.home_page.enter_product_into_search_box_field("")