from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.PageObject import PageObject


class CustomersPage(PageObject):

    # Locators
    search_customer = 'input[ng-model="searchCustomer"]'
    text_first_name = "Ana"
    text_last_name = "Souza"
    text_post_code = '123456'
    text_account = '1016'
    column_first_name = 'td[class=ng-binding], Ana'
    column_last_name = 'tbody tr:nth-child(1) td:nth-child(2)'
    column_post_code = 'tbody tr:nth-child(1) td:nth-child(3)'
    column_account = 'tbody span:nth-child(1)'
    btn_delete_customer = 'button[ng-click="deleteCust(cust)"]'

    def search_customers_first_name(self):
        self.driver.find_element(By.CSS_SELECTOR, self.search_customer).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.search_customer).click()
        self.driver.find_element(By.CSS_SELECTOR, self.search_customer).send_keys(self.text_first_name)

    def search_customers_last_name(self):
        self.driver.find_element(By.CSS_SELECTOR, self.search_customer).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.search_customer).click()
        self.driver.find_element(By.CSS_SELECTOR, self.search_customer).send_keys(self.text_last_name)

    def search_customers_post_code(self):
        self.driver.find_element(By.CSS_SELECTOR, self.search_customer).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.search_customer).click()
        self.driver.find_element(By.CSS_SELECTOR, self.search_customer).send_keys(self.text_post_code)

    def search_customers_account(self):
        self.driver.find_element(By.CSS_SELECTOR, self.search_customer).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.search_customer).click()
        self.driver.find_element(By.CSS_SELECTOR, self.search_customer).send_keys(self.text_account)

    def check_value_column_first_name(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.column_first_name).text == self.text_first_name

    def check_value_column_last_name(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.column_last_name).text == self.text_last_name

    def check_value_column_post_code(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.column_post_code).text == self.text_post_code

    def check_value_column_account(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.column_account).text == self.text_account

    def click_customer_delete(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btn_delete_customer).click()

    def check_customer_clean_list(self):
        try:
            return self.driver.find_element(By.CSS_SELECTOR, self.btn_delete_customer).is_displayed()
        except NoSuchElementException:
            return True



