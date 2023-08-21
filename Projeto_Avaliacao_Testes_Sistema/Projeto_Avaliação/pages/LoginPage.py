from selenium.webdriver.common.by import By
from pages.PageObject import PageObject


class LoginPage(PageObject):

    # Locators
    url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'
    btn_manager = 'button[ng-click="manager()"]'
    login_button = 'button[ng-click="customer()"]'

    # Services
    def __init__(self, browser):
        super(LoginPage, self).__init__(browser=browser)
        self.driver.get(self.url)

    def click_login_btn_customer(self):
        self.driver.find_element(By.CSS_SELECTOR, self.login_button).click()

    def click_login_btn_manager(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btn_manager).click()

    def is_url_login(self):
        return self.driver.current_url == self.url
