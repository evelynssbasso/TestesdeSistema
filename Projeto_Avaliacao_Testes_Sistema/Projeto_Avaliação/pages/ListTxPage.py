from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.PageObject import PageObject


class ListTxPage(PageObject):

    # Locators
    url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/listTx'
    css_validate_value_deposit = '#anchor0 > td:nth-child(2)'
    value_deposit = '15000'
    value_deposit_native = '30'
    css_validate_value_withdrawl = '#anchor1 > td:nth-child(2)'
    value_withdrawl = '7000'
    value_withdrawl_native = '4'
    css_validate_type_credit = '#anchor0 > td:nth-child(3)'
    type_deposit = 'Credit'
    css_validate_type_debit = '#anchor1 > td:nth-child(3)'
    type_debit = 'Debit'
    information_transactions = 'tr.ng-scope'

    def check_list_value_deposit(self):
        check_deposit = \
            (self.driver.find_element(By.CSS_SELECTOR, self.css_validate_value_deposit).text
             == self.value_deposit)
        return check_deposit

    def check_list_value_deposit_native(self):
        check_deposit = \
            (self.driver.find_element(By.CSS_SELECTOR, self.css_validate_value_deposit).text
             == self.value_deposit_native)
        return check_deposit

    def check_list_type_credit(self):
        check_type_credit = \
            (self.driver.find_element(By.CSS_SELECTOR, self.css_validate_type_credit).text
             == self.type_deposit)
        return check_type_credit

    def check_list_value_withdrawl(self):
        check_withdrawl = \
            (self.driver.find_element(By.CSS_SELECTOR, self.css_validate_value_withdrawl).text
             == self.value_withdrawl)
        return check_withdrawl

    def check_list_value_withdrawl_native(self):
        check_withdrawl = \
            (self.driver.find_element(By.CSS_SELECTOR, self.css_validate_value_withdrawl).text
             == self.value_withdrawl_native)
        return check_withdrawl

    def check_list_type_debit(self):
        check_type_debit = \
            (self.driver.find_element(By.CSS_SELECTOR, self.css_validate_type_debit).text
             == self.type_debit)
        return check_type_debit

    def is_url_transactions(self):
        return WebDriverWait(self.driver.current_url == self.url, 3)
