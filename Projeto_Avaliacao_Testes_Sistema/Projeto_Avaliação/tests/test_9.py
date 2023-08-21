from pages.AccountPage import AccountPage
from pages.ListTxPage import ListTxPage
from pages.LoginCustomerPage import LoginCustomerPage

class Test9:

    def test_list_transactions_account_customer(self, setup):
        login_page = setup
        assert login_page.is_url_login(), "Página inicial errada!"
        login_page.click_login_btn_customer()
        login_customer = LoginCustomerPage(driver=login_page.driver)
        login_customer.list_customers()
        login_customer.select_login_customer_nativo()
        login_customer.click_button_login_customer()
        account_customer = AccountPage(driver=login_customer.driver)
        account_customer.click_button_transactions()
        list_transactions = ListTxPage(driver=account_customer.driver)
        assert list_transactions.is_url_transactions(), 'Pagina nao encontrada'
        assert list_transactions.check_list_value_deposit_native(), 'Valor na lista do deposito incoerente'
        assert list_transactions.check_list_type_credit(), 'Type na lista do deposito incoerente'
        assert list_transactions.check_list_value_withdrawl_native(), 'Valor na lista de retirada incoerente'
        assert list_transactions.check_list_type_debit(), 'Type na lista de retirada incoerente'
