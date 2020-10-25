from behave import given, when, then
from features.lib.pages.login import Login
from features.lib.pages.products import Products


@given(u'I open Lojinha')
def step_impl(context):
    login_page = Login(context)
    login_page.launch()


@when(u'I insert the "{user}" and "{pwd}"')
def step_impl(context, user, pwd):
    login_page = Login(context)
    login_page.set_user(user)
    login_page.set_password(pwd)


@when(u'I click on ENTRAR')
def step_impl(context):
    login_page = Login(context)
    login_page.click_login()


@then(u'the user is granteed to the website')
def step_impl(context):
    products = Products(context)
    assert products.is_in_screen()


@then(u'the user is not allowed to login the website')
def step_impl(context):
    login_page = Login(context)
    assert login_page.is_toast()
