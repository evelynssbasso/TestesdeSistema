from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class LoginCustomerPage(PageObject):

    # Locators
    url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/customer'
    select_customer = 'select[ng-model="custId"]'
    choose_customer_nativo = 'option[value="1"]'
    choose_customer = 'option[value="6"]'
    btn_login = 'button[type="submit"]'

    def list_customers(self):
        self.driver.find_element(By.CSS_SELECTOR, self.select_customer).click()

    def select_login_customer(self):
        self.driver.find_element(By.CSS_SELECTOR, self.choose_customer).click()
        self.driver.find_element(By.CSS_SELECTOR, self.select_customer).click()

    def select_login_customer_nativo(self):
        self.driver.find_element(By.CSS_SELECTOR, self.choose_customer_nativo).click()
        self.driver.find_element(By.CSS_SELECTOR, self.select_customer).click()

    def click_button_login_customer(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btn_login).click()
