from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


from pages.PageObject import PageObject


class ManagerPage(PageObject):

    # Locators
    url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager'
    btn_add_customer = 'button[ng-click="addCust()"]'
    btn_open_account = 'button[ng-click="openAccount()"]'
    btn_customers = 'button[ng-click="showCust()"]'

    def __init__(self, driver):
        super(ManagerPage, self).__init__(driver=driver)
        self.driver = driver

    # botão que cadastra o cliente
    def click_btn_add_customer(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btn_add_customer).click()

    # botão que vincula o cliente a moeda corrente para o uso das transações
    def click_btn_open_account(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btn_open_account).click()

    # botão para gerenciar o cadastro das contas do cliente
    def click_btn_customers(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btn_customers).click()

    def is_url_manager(self):
        return WebDriverWait(self.driver.current_url == self.url, 3)
