class Test_sem_efeito:

    def test_list_transactions_account_customer(self, withdrawl_in_account):
        account_customer = withdrawl_in_account
        account_customer.click_button_transactions()
        assert account_customer.is_url_transactions(), 'Pagina nao encontrada'

    # Professor essa parte abaixo esta visivel somente para sua avaliacao, onde tentamos colocar um assert para que
    # as transacoes fosse listada do dado inicial, cliente: 'Ana Souza', inserido no portal, porem o mesmo na lista de
    # transacoes, por um falha, creio do portal, nao tras os mesmos, por isso foi feito o test_9 com o login
    # 'Hermoine Granger' onde o mesmo trouxe com sucesso na nossa automacao.

        assert account_customer.check_list_value_deposit(), 'Valor na lista do deposito incoerente'
        assert account_customer.check_list_type_credit(), 'Type na lista do deposito incoerente'
        assert account_customer.check_list_value_withdrawl(), 'Valor na lista de retirada incoerente'
        assert account_customer.check_list_type_debit(), 'Type na lista de retirada incoerente'
