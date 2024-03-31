import datetime
def client_has_enough_sum(client, amount):
    return client['account'] >= amount

class Transaction:
    def __init__(self, date_transaction, amount, sender, receiver):
        self._status             = 'Init'
        self._date_transaction   = date_transaction
        self._amount             = amount
        self._sender             = sender
        self._receiver           = receiver

    def set_status_in_progress(self):
        self._status = 'In progress'

    def execute_transaction(self):
        if client_has_enough_sum(self._sender, self._amount):

            self._sender['account']     -=  self._amount
            self._receiver['account']   += self._amount

            self._status = "Finished successfully"
        else:
            self._status = "Insufficient funds" #Недостаточно средств

    def finish_transacion(self):
        if self._status == "Finished successfully":
            self._status = 'Done'
        else:
            self._status = 'Cancelled'

    def show_info_about_transaction(self):
        print(f'Status: {self._status}; Sender: {self._sender}; Receiver: {self._receiver}')

class TransactionManager:
    def __init__(self):
        self._transaction_list = []

    def start_new_transaction(self, date_transaction, amount, sender, receiver):
        self._transaction_list.append(Transaction(date_transaction, amount, sender, receiver))
        transaction_id = len(self._transaction_list)-1
        self._transaction_list[transaction_id].set_status_in_progress()
        return transaction_id

    def complete_transaction(self, transaction_id):
        transaction = self._transaction_list[transaction_id]

        transaction.execute_transaction()
        transaction.finish_transacion()
    def show_all_transactions(self):
        for transaction in self._transaction_list:
            print(f'ID: {self._transaction_list.index(transaction)}')
            transaction.show_info_about_transaction()

if __name__ == '__main__':

    client1 = {'name': "Ivan",
               'account': 10000}
    client2 = {'name': "Petr",
               'account': 15000}

    current_time = datetime.datetime.now()

    transaction_manager = TransactionManager()

    amount = 5000
    id1 = transaction_manager.start_new_transaction(current_time, amount, client1, client2)

    amount = 10000
    id2 = transaction_manager.start_new_transaction(current_time, amount, client1, client2)

    print('Транзакции перед выполнением:')
    transaction_manager.show_all_transactions()

    transaction_manager.complete_transaction(id1)
    transaction_manager.complete_transaction(id2)

    print('')
    print('Транзакции после выполнения:')
    transaction_manager.show_all_transactions()
