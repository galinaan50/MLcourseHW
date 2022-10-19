# ------------------------------ class definition ----------------------------- #
class BankAcount:
	def __init__(self,name,balance ):
		self.owner=name
		self.balance=balance

	def depostit(self,x):
		self.balance+=x

# ------------------- create BankAcount objects (instances) ------------------ #
maria_account=BankAcount('Maria', 1000)
pesho_account=BankAcount('Pesho', 2000)


# maria_account.owner = 'Maria'
# maria_account.balance = 1000

# pesho_account.owner = 'Pesho'
# pesho_account.balance = 2000;


maria_account.depostit(700) # deposit(maria_account, 700)
pesho_account.depostit(100) # deposit(pesho_accoutt, 100)

print(maria_account.balance) # 1700
print(pesho_account.balance) # 2100





# accounts = [maria_account, pesho_account]

# for account in accounts:
# 	print(account.balance)