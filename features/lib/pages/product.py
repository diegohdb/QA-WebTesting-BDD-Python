from selenium.webdriver.common.by import By
from features.lib.pages.base import BasePage


class Product(BasePage):

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser,
            base_url='http://165.227.93.41/lojinha-web/produto/novo')

    et_product_name = By.ID, 'produtonome'
    et_product_value = By.ID, 'produtovalor'
    et_product_colors = By.ID, 'produtocores'
    bt_save = By.XPATH, '/html/body/div[2]/div/div/form/div[5]/button'
    toast = By.XPATH, '//*[@id="toast-container"]/div'

    def set_name(self, product_name):
        self.send_text(self.et_product_name, product_name)

    def set_value(self, product_value):
        self.send_text(self.et_product_value, product_value)

    def set_colors(self, product_colors):
        self.send_text(self.et_product_colors, product_colors)

    def save(self):
        self.click(self.bt_save)

    def get_toast_message(self):
        return self.get_elem(self.toast).text
