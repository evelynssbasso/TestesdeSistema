
class Test4:

    def test_delete_customer(self, manager_customers):
        customers = manager_customers
        customers.click_customer_delete()
        assert customers.check_customer_clean_list(), "Customer localizado"


