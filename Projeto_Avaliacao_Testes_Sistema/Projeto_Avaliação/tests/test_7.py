class Test7:

    def test_withdrawl_account_customer_insuccess(self, deposit_in_account):
        account_customer = deposit_in_account
        account_customer.click_button_withdrawl()
        account_customer.insert_value_amount_withdrawl('30000')
        account_customer.click_save_withdrawl()
        assert account_customer.check_message_transaction('Transaction Failed. You can not withdraw amount more than the balance.'), 'Problema ao efetivar a transacao'
        assert account_customer.check_balance_account('15000'), 'Saldo incorreto'

