from pages.AccountPage import AccountPage
from pages.LoginCustomerPage import LoginCustomerPage


class Test6:

    def test_deposit_account_customer(self, add_account, setup):
        login_page = setup
        manager_page, add_customer_page = add_account
        manager_page.click_btn_home()
        login_page.click_login_btn_customer()
        login_customer = LoginCustomerPage(driver=login_page.driver)
        login_customer.list_customers()
        login_customer.select_login_customer()
        login_customer.click_button_login_customer()
        account_customer = AccountPage(driver=login_page.driver)
        assert account_customer.is_url_account(), 'Pagina nao encontrada'
        assert account_customer.check_account_customer(), 'Pagina nao encontrada'
        assert account_customer.check_balance_account('0'), 'Balance nao esperado'
        account_customer.click_button_deposit()
        account_customer.insert_value_amount_deposit('15000')
        account_customer.click_save_deposit()
        assert account_customer.check_message_transaction('Deposit Successful'), 'Problema ao efetivar a transacao'
        assert account_customer.check_balance_account('15000'), 'Saldo incorreto'

