class BankAccount:
    def __init__(self,balance=0):
        self.__balance = balance


    def get_balance(self):
        return self.__balance
    
    def deposite(self,amount):
        if amount > 0:
            self.__balance+=amount
            print(f"{amount} EUR noguldīti kontā.")
        else:
            print("Noguldīšanas summa jābūt pozitīvai.")
    def witdraw(self,amount):
        if amount > self.__balance:
            print("Nepieteikami līdzekļi izņemānai.")
        elif amount <=0:
            print("Izņemšanas summa jabūt pozitīvai.")
        else:
            self.__balance -= amount
            print(f"{amount} Eur izņemti no konta.")
account= BankAccount(100)
print("Pašreizējais atlikums:  ",account.get_balance())
account.deposite(50)
print("PAšreizējais atlikums pēc noguldījuma:",account.get_balance())
account.witdraw(10)