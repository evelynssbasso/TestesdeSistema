from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By


class PageObject:

    # Locators
    btn_home = 'button[ng-click="home()"]'

    def __init__(self, driver=None, browser=None):
        if driver:
            self.driver = driver
        else:
            if browser == 'chrome':
                self.driver = webdriver.Chrome()
            elif browser == 'edge':
                self.driver = webdriver.Edge()
            elif browser == 'firefox':
                self.driver = webdriver.Firefox()
            else:
                raise Exception('Browser não suportado')
            # self.driver.maximize.window()
            self.driver.implicitly_wait(3)

    # def close(self):
    #     self.driver.quit()

    def is_url(self, url):
        return self.driver.current_url == url

    def conf_alert(self):
        alert = Alert(self.driver)
        alert_text = alert.text
        print(alert_text)
        if alert_text.find("successfully") != -1:
            alert.accept()
            return True
        else:
            return False

    def click_btn_home(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btn_home).click()

