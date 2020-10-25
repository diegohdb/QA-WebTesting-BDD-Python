from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:

    def __init__(self, browser, base_url='http://www.seleniumframework.com'):
        self.base_url = base_url
        self.browser = browser
        self.timeout = 30

    def get_elem(self, by_locator, waitfor=20):
        return WebDriverWait(self.browser, waitfor).until(EC.visibility_of_element_located(by_locator))

    def get_elements(self, by_locator, waitfor=20):
        elements = WebDriverWait(self.browser, waitfor).until(EC.visibility_of_all_elements_located(by_locator))
        return elements

    def send_text(self, locator, text):
        return WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def click(self, by_locator):
        WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def find_element(self, *loc):
        return self.browser.find_element(*loc)

    def visit(self, url):
        self.browser.get(url)

    def delete_by_index(self, index):
        locator = f'/html/body/div[2]/div/ul/li[{index}]/a'
        by_locator = By.XPATH, locator
        WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def click_product_by_index(self, index):
        locator = f'/html/body/div[2]/div/ul/li[{index}]/span/a'
        by_locator = By.XPATH, locator
        WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(by_locator)).click()
