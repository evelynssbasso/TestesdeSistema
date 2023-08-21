import time

from pages.AddCustomerPage import AddCustomerPage
from pages.ManagerPage import ManagerPage


class Test1:

    def test_add_customer(self, setup):
        login_page = setup
        assert login_page.is_url_login(), "Página inicial errada!"

        login_page.click_login_btn_manager()

        manager_page = ManagerPage(driver=login_page.driver)
        assert manager_page.is_url_manager(), "Página mudou!"
        manager_page.click_btn_add_customer()
        add_customer_page = AddCustomerPage(driver=login_page.driver)
        add_customer_page.insert_customer()

        assert add_customer_page.conf_alert(), "Cadastro não realizado"

