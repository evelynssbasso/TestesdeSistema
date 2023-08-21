from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from pages.PageObject import PageObject


class AddCustomerPage(PageObject):

    # Locators
    url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/addCust'
    login_button = 'login-button'
    login_error_message = '[data-test="error"]'
    txt_login_error_massage = 'Epic sadface: Username is required'
    first_name = 'input[ng-model="fName"]'
    last_name = 'input[ng-model="lName"]'
    post_code = 'input[ng-model="postCd"]'
    btn_save_customer = '[type="submit"]'

    # Services
    def __init__(self, driver):
        super(AddCustomerPage, self).__init__(driver=driver)
        self.driver = driver

    def is_url_add_customer(self):
        return self.driver.current_url == self.url

    def click_btn_save_customer(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btn_save_customer).click()

    def insert_customer(self, text_first_name="Ana", text_last_name="Souza", text_post_code='123456'):
        self.driver.find_element(By.CSS_SELECTOR, self.first_name).send_keys(text_first_name)
        self.driver.find_element(By.CSS_SELECTOR, self.last_name).send_keys(text_last_name)
        self.driver.find_element(By.CSS_SELECTOR, self.post_code).send_keys(text_post_code)
        self.click_btn_save_customer()
