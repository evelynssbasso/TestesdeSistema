from pages.OpenAccountPage import OpenAccountPage

class Test2:

    def test_add_account(self, add_customer):
        login_page, manager_page, add_customer_page = add_customer
        manager_page.click_btn_open_account()
        open_account = OpenAccountPage(driver=manager_page.driver)
        open_account.list_customers()
        open_account.list_choose_customer()
        open_account.list_currency()
        open_account.list_choose_currency()
        open_account.click_button_process_account()
        assert open_account.conf_alert(), "Conta não cadastrada"



