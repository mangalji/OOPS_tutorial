from abc import ABC, abstractmethod

class Bank_Account_Management(ABC):
	def __init__(self):#,name,acc_no,balance):
		# self.name = name
		# self.__acc_no = acc_no
		# self.balance = balance
		self.name = input('enter the customer name : ')
		self.__acc_no = input("enter the account number of customer: ")
		self.balance = int(input("enter the balance amount in customer's bank account: "))
		print(f"Account Holder Name: {self.name}")
		print(f"Account Number: {self.__acc_no}")
		print(f"Bank Balance: {self.balance}")

	@abstractmethod
	def account_type(self):
		pass

	def deposit(self):#,amount):
		amount = int(input("enter the deposit amount: "))
		self.balance += amount
		print(f"RS{amount} deposited. New balance = RS{self.balance}")

	def withdraw(self):#,amount):
		amount = int(input("enter the withdraw amount: "))
		if amount<=self.balance:
			self.balance -= amount
			print(f"RS{amount} withdraw. Remaining balance = RS{self.balance}")
		else:
			print("Insufficient Balance!!")

	def show_balance(self):
		print(f"Account Holder: {self.name}")
		print(f"Current Bank Balance: {self.balance}")

class Savings_account(Bank_Account_Management):
	def account_type(self):
		print('Savings Account')
class Current_account(Bank_Account_Management):
	def account_type(self):
		print('Current Account')
class Loan_account(Bank_Account_Management):
	def account_type(self):
		print('Loan Account')

def select_account():
	true = True
	while true == True:
		choose_bank_account_type = input("which account type: Savings/Current/Loan")
		if choose_bank_account_type == 'Savings' or choose_bank_account_type == 'savings':
			A1 = Savings_account()
			A1.account_type()
			action = input("which action you want to perform:\nPress 1 for Deposit money\nPress 2 for Withdraw money\nPress 3 for skip the process.\n press button accordingly: ")
			if action == '1':
				A1.deposit()
				A1.show_balance()
				print("Bank account details updated successfully..")
				print("\n===========================\n")
				true = False

			elif action == '2':
				A1.withdraw()
				A1.show_balance()
				print("Bank account details updated successfully..")
				print("\n===========================\n")
				true = False
			else:
				true = False
		elif choose_bank_account_type == 'Current' or choose_bank_account_type == 'current':	
			A1 = Current_account()
			A1.account_type()
			action = input("which action you want to perform:\nPress 1 for Deposit money\nPress 2 for Withdraw money\nPress 3 for skip the process.\n press button accordingly: ")
			if action == '1':
				A1.deposit()
				A1.show_balance()
				print("Bank account details updated successfully..")
				print("\n===========================\n")
				true = False

			elif action == '2':
				A1.withdraw()
				A1.show_balance()
				print("Bank account details updated successfully..")
				print("\n===========================\n")
				true = False
			else:
				true = False
		elif choose_bank_account_type == 'Loan' or choose_bank_account_type == 'loan':
			A1 = Loan_account()
			A1.account_type()
			action = input("which action you want to perform:\nPress 1 for Deposit money\nPress 2 for Withdraw money\nPress 3 for skip the process.\n press button accordingly: ")
			if action == '1':
				A1.deposit()
				A1.show_balance()
				print("Bank account details updated successfully..")
				print("\n===========================\n")
				true = False

			elif action == '2':
				A1.withdraw()
				A1.show_balance()
				print("Bank account details updated successfully..")
				print("\n===========================\n")
				true = False
			else:
				true = False
		else:
			print('Invalid Choice')
			continue
	else:
		print("Thank you for using Bank Account Management System..")
		
select_account()

continue_ = True
while continue_ == True:
	modify = input('Do you want to modify another bank account if Yes press Y if No N: ')
	if modify == 'Y' or modify == 'y':
		select_account()
	else:
		print("Thank you for using Bank Account Management System..")
		# true == False
		break
