from selenium.webdriver.common.by import By
from features.lib.pages.base import BasePage
from features.lib.pages.product import Product


class ProductEdition(BasePage):

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser,
            base_url='http://165.227.93.41/lojinha-web/produto')
        self.product = Product(context)

    tv_product_edition = By.XPATH, '/html/body/div[2]/div/div/div[1]/h4'
    bt_add_component = By.XPATH, '/html/body/div[2]/div/div/div[3]/div[1]/a'
    bt_list = By.XPATH, '/html/body/div[2]/div/div/div[3]/form/div[4]/a'
    tv_product_name = By.ID, 'produtonome'
    tv_product_value = By.ID, 'produtovalor'
    tv_product_colors = By.ID, 'produtocores'

    def is_in_screen(self):
        return self.get_elem(self.tv_product_edition)

    def add_product(self):
        self.click(self.bt_add_component)

    def list_products(self):
        self.click(self.bt_list)

    def get_name(self):
        return self.get_elem(self.tv_product_name).get_attribute('value')

    def get_value(self):
        return self.get_elem(self.tv_product_value).get_attribute('value')

    def get_colors(self):
        return self.get_elem(self.tv_product_colors).get_attribute('value')
