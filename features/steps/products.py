from behave import given, when, then
from features.lib.pages.login import Login
from features.lib.pages.product import Product
from features.lib.pages.product_edition import ProductEdition
from features.lib.pages.products import Products


@given(u'I insert the "{user}" and "{pwd}"')
def step_impl(context, user, pwd):
    login_page = Login(context)
    login_page.set_user(user)
    login_page.set_password(pwd)


@given(u'I click on ENTRAR')
def step_impl(context):
    login_page = Login(context)
    login_page.click_login()


@given(u'I click on ADICIONAR PRODUTO')
def step_impl(context):
    products_page = Products(context)
    products_page.add_product()


@given(u'I insert "{product_name}", "{product_value}", "{product_colors}"')
def step_impl(context, product_name, product_value, product_colors):
    product_page = Product(context)
    product_page.set_name(product_name)
    product_page.set_value(product_value)
    product_page.set_colors(product_colors)


@when(u'I click on SALVAR')
def step_impl(context):
    product_page = Product(context)
    product_page.save()


@then(u'a toast shows the register confirmation and the product edition page is loaded')
def step_impl(context):
    product_page = Product(context)
    product_edition_page = ProductEdition(context)
    assert product_page.get_toast_message() == 'Produto adicionado com sucesso'
    assert product_edition_page.is_in_screen()


@given(u'I insert "{product_name}"')
def step_impl(context, product_name):
    product_page = Product(context)
    product_page.set_name(product_name)


@then(u'the product list is loaded and the "{product_name}" is not added')
def step_impl(context, product_name):
    products_page = Products(context)
    assert not product_name in products_page.get_all_products()


@given(u'I click on SALVAR')
def step_impl(context):
    product_page = Product(context)
    product_page.save()


@given(u'I go to products list')
def step_impl(context):
    product_edition_page = ProductEdition(context)
    product_edition_page.list_products()


@when(u'I delete the "{product_name}"')
def step_impl(context, product_name):
    products_page = Products(context)
    products_page.delete_product(product_name)


@then(u'a toast shows the delete confirmation and the "{product_name}" is not is seen in the product list')
def step_impl(context, product_name):
    products_page = Products(context)
    assert products_page.get_toast_message() == 'Produto removido com sucesso'
    assert not product_name in products_page.get_all_products()


@when(u'I click on the "{product_name}"')
def step_impl(context, product_name):
    products_page = Products(context)
    products_page.see_product(product_name)


@then(u'the Edit product page is loaded with "{product_name}", "{product_value}", and "{product_colors}"')
def step_impl(context, product_name, product_value, product_colors):
    product_edition = ProductEdition(context)
    product_value = f'{product_value[:-2]},{product_value[-2:]}'
    assert product_edition.get_name() == product_name
    assert product_edition.get_value() == product_value
    assert product_edition.get_colors() == product_colors
