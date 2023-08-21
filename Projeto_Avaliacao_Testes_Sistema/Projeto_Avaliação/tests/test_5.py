import time

from pages.AccountPage import AccountPage
from pages.LoginCustomerPage import LoginCustomerPage


class Test5:

    def test_login_with_account_not_registered(self, add_customer):
        login_page, manager_page, open_account = add_customer
        manager_page.click_btn_home()
        login_page.click_login_btn_customer()
        login_customer = LoginCustomerPage(driver=login_page.driver)
        login_customer.list_customers()
        login_customer.select_login_customer()
        login_customer.click_button_login_customer()
        account_customer = AccountPage(driver=login_page.driver)
        assert account_customer.is_url_account(), 'Pagina nao encontrada'
        assert account_customer.check_not_account(), 'Customer com conta cadastrada'
        time.sleep(3)
