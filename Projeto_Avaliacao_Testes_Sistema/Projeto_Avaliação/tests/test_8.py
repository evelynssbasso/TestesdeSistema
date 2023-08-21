class Test8:

    def test_withdrawl_account_customer_success(self, deposit_in_account):
        account_customer = deposit_in_account
        account_customer.click_button_withdrawl()
        account_customer.insert_value_amount_withdrawl('7000')
        account_customer.click_save_withdrawl()
        assert account_customer.check_message_transaction('Transaction successful'), 'Problema ao efetivar a transacao'
        assert account_customer.check_balance_account('8000'), 'Saldo incorreto'