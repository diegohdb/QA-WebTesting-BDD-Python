from selenium.webdriver.common.by import By
from features.lib.pages.base import BasePage
from features.lib.pages.product import Product


class Products(BasePage):

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser,
            base_url='http://165.227.93.41/lojinha-web/produto')
        self.product = Product(context)

    tv_list_products = By.XPATH, '/html/body/div[2]/div/h3'
    bt_add_product = By.XPATH, '/html/body/div[2]/div/div/a'
    ul_products = By.XPATH, '/html/body/div[2]/div/ul'
    product_names = By.XPATH, '/html/body/div[2]/div/ul/li/span/a'
    toast = By.XPATH, '//*[@id="toast-container"]/div'

    def is_in_screen(self):
        return self.get_elem(self.tv_list_products)

    def add_product(self):
        self.click(self.bt_add_product)

    def get_all_products(self):
        products = self.get_elements(self.product_names)
        return products

    def delete_product(self, product):
        products = self.get_elements(self.product_names)
        for i, element in enumerate(products):
            if element.text == product:
                self.delete_by_index(i+1)

    def get_toast_message(self):
        return self.get_elem(self.toast).text

    def see_product(self, product):
        products = self.get_elements(self.product_names)
        for i, element in enumerate(products):
            if element.text == product:
                self.click_product_by_index(i + 1)
