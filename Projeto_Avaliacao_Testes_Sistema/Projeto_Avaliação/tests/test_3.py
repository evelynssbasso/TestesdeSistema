from pages.CustomersPage import CustomersPage


class Test3:

    def test_manager_customers(self, add_account):
        manager_page, open_account = add_account
        manager_page.click_btn_customers()
        customers = CustomersPage(driver=manager_page.driver)
        customers.search_customers_first_name()
        assert customers.check_value_column_first_name(), "Customer nao localizado"
        customers.search_customers_last_name()
        assert customers.check_value_column_last_name(), "Customer nao localizado"
        customers.search_customers_post_code()
        assert customers.check_value_column_post_code(), "Customer nao localizado"
        customers.search_customers_account()
        assert customers.check_value_column_account(), "Customer nao localizado"
