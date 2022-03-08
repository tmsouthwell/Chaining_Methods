class User:
    def __init__(self, first_name, last_name, account_balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account_balance = account_balance

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def make_deposit(self,amount):
        self.account_balance += amount
        return self

    def display_user_balance(self):
        print(f"User: {self.first_name}, Balance: {self.account_balance}")
        return self

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self
        
        
bob = User("Bob", "Smith", 500)
print(bob.account_balance)

guido = User("Guido", "Parma", 1000)
print(guido.account_balance)



guido.make_withdrawal(100).make_deposit(200).make_deposit(150).display_user_balance()
bob.transfer_money(guido, 100).display_user_balance()

guido.display_user_balance()

# print(guido.account_balance)
# print(guido.account_balance)


