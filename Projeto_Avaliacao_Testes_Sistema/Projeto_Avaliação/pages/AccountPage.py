from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.PageObject import PageObject


class AccountPage(PageObject):

    # Locators
    url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/account'
    css_not_account = 'span[ng-show="noAccount"]'
    msg_not_account = "Please open an account with us."
    css_account_customer = 'div:nth-child(3) > strong:nth-child(1)'
    css_balance_account = 'div:nth-child(3) > strong:nth-child(2)'
    number_account_customer = '1016'
    btn_deposit = 'button[ng-click="deposit()"]'
    hab_btn_deposit = 'button.btn-primary[ng-click="deposit()"]'
    css_campo_value_amount_deposit = 'form[name="myForm"][ng-submit="deposit()"] input[ng-model="amount"]'
    css_campo_value_amount_withdrawl = 'form[name="myForm"][ng-submit="withdrawl()"] input[ng-model="amount"]'
    btn_save_deposit = 'form[name="myForm"][ng-submit="deposit()"] button[type=submit]'
    btn_save_withdrawl = 'form[name="myForm"][ng-submit="withdrawl()"] button[type=submit]'
    css_message_transaction = 'span[ng-show=message]'
    btn_withdrawl = 'button[ng-click="withdrawl()"]'
    hab_btn_withdrawl = 'button.btn-primary[ng-click="withdrawl()"]'
    btn_transactions = 'button[ng-click="transactions()"]'

    def is_url_account(self):
        return WebDriverWait(self.driver.current_url == self.url, 3)

    def check_not_account(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.css_not_account).text == self.msg_not_account

    def check_account_customer(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.css_account_customer).text == self.number_account_customer

    def check_balance_account(self, balance):
        return self.driver.find_element(By.CSS_SELECTOR, self.css_balance_account).text == balance

    def click_button_deposit(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btn_deposit).click()
        wait = WebDriverWait(self.driver, 4)
        element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.hab_btn_deposit)))
        wait.until(EC.visibility_of(element))

    def insert_value_amount_deposit(self, value_amount):
        self.driver.find_element(By.CSS_SELECTOR, self.css_campo_value_amount_deposit).send_keys(value_amount)

    def click_save_deposit(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btn_save_deposit).click()

    def click_button_withdrawl(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btn_withdrawl).click()
        wait = WebDriverWait(self.driver, 4)
        element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.hab_btn_withdrawl)))
        wait.until(EC.visibility_of(element))

    def insert_value_amount_withdrawl(self, value_amount):
        self.driver.find_element(By.CSS_SELECTOR, self.css_campo_value_amount_withdrawl).send_keys(value_amount)

    def click_save_withdrawl(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btn_save_withdrawl).click()

    def check_message_transaction(self, message):
        return self.driver.find_element(By.CSS_SELECTOR, self.css_message_transaction).text == message

    def click_button_transactions(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btn_transactions).click()

