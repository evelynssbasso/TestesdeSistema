from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class OpenAccountPage(PageObject):

    # Locators
    select_customer = 'select[ng-model="custId"]'
    choose_customer = 'option[value="6"]'
    select_currency = 'currency'
    choose_currency = 'option[value="Dollar"]'
    btn_process = 'button[type="submit"]'

    def list_customers(self):
        self.driver.find_element(By.CSS_SELECTOR, self.select_customer).click()

    def list_choose_customer(self):
        self.driver.find_element(By.CSS_SELECTOR, self.choose_customer).click()
        self.driver.find_element(By.CSS_SELECTOR, self.select_customer).click()

    def list_currency(self):
        self.driver.find_element(By.ID, self.select_currency).click()

    def list_choose_currency(self):
        self.driver.find_element(By.CSS_SELECTOR, self.choose_currency).click()

    def click_button_process_account(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btn_process).click()
