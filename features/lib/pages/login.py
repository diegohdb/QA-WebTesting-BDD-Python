from selenium.webdriver.common.by import By
from features.lib.pages.base import BasePage


class Login(BasePage):

    et_user = By.ID, 'usuario'
    et_pwd = By.ID, 'senha'
    bt_login = By.XPATH, '/html/body/div[2]/div[1]/div/form/div[4]/div/button'
    toast = By.XPATH, '//*[@id="toast-container"]/div'

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser,
            base_url='http://165.227.93.41/lojinha-web/')

    def launch(self):
        self.visit(self.base_url)

    def set_user(self, user):
        self.send_text(self.et_user, user)

    def set_password(self, pwd):
        self.send_text(self.et_pwd, pwd)

    def click_login(self):
        self.click(self.bt_login)

    def is_toast(self):
        return self.get_elem(self.toast, waitfor=20)
