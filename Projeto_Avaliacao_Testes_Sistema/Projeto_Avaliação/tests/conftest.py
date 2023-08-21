
import pytest

from pages.AccountPage import AccountPage
from pages.CustomersPage import CustomersPage
from pages.LoginCustomerPage import LoginCustomerPage
from pages.LoginPage import LoginPage
from pages.AddCustomerPage import AddCustomerPage
from pages.ManagerPage import ManagerPage
from pages.OpenAccountPage import OpenAccountPage


@pytest.fixture
def setup(select_browser):
    login_page = LoginPage(browser=select_browser)
    yield login_page

def pytest_addoption(parser):
    parser.addoption("--select_browser", default="chrome", help="Select browser")

@pytest.fixture
def select_browser(request):
    yield request.config.getoption("--select_browser").lower()

@pytest.fixture
def add_customer(setup):
    login_page = setup
    login_page.click_login_btn_manager()
    manager_page = ManagerPage(driver=login_page.driver)
    manager_page.click_btn_add_customer()
    add_customer_page = AddCustomerPage(driver=login_page.driver)
    add_customer_page.insert_customer()
    assert add_customer_page.conf_alert(), "Cadastro não realizado"
    yield login_page, manager_page, add_customer_page

@pytest.fixture
def add_account(add_customer):
    login_page, manager_page, add_customer_page = add_customer
    manager_page.click_btn_open_account()
    open_account = OpenAccountPage(driver=manager_page.driver)
    open_account.list_customers()
    open_account.list_choose_customer()
    open_account.list_currency()
    open_account.list_choose_currency()
    open_account.click_button_process_account()
    assert add_customer_page.conf_alert(), "Conta não cadastrada"
    yield manager_page, open_account

@pytest.fixture
def manager_customers(add_account):
    manager_page, open_account = add_account
    manager_page.click_btn_customers()
    customers = CustomersPage(driver=manager_page.driver)
    customers.search_customers_first_name()
    assert customers.check_value_column_first_name(), "Customer nao localizado"
    yield customers

@pytest.fixture
def deposit_in_account(add_account, setup):
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
    yield account_customer

@pytest.fixture
def withdrawl_in_account(deposit_in_account):
    account_customer = deposit_in_account
    account_customer.click_button_withdrawl()
    account_customer.insert_value_amount_withdrawl('7000')
    account_customer.click_save_withdrawl()
    assert account_customer.check_message_transaction('Transaction successful'), 'Problema ao efetivar a transacao'
    assert account_customer.check_balance_account('8000'), 'Saldo incorreto'
    yield account_customer
