class User:
    def __init__(self, pin_code, balance):
        self.pin_code = pin_code
        self.balance = balance
        
    def password_check(self, pin):
        if pin != self.pin_code:
            return False
        else:
            return True
            
    def getBalance(self):
        return self.balance
    
    def withdraw_process(self, withdrawAmount):
        if withdrawAmount > self.balance:
            return False
        else:
            self.balance -= withdrawAmount
            return True
            
    def deposit_process(self, depositAmount):
        self.balance += depositAmount
        return self.balance
        
class ATM:
    def __init__(self, current_user):
        self.current_user = current_user

    def input_pin(self):
        while True:
            pin = input("pinを入力：").strip().replace(" ","")
            
            if not pin.isdigit() or len(pin) != 4:
                print("4つの数字だけにしろ")
                continue

            if not self.current_user.password_check(pin):
                print("pinは違うよ")
            else:
                print("pinは正解")
                break

    def withdraw_request(self):
        amount = input("引き出す金額を入力：").strip().replace(" ","")
        if not amount.isdigit():
            print("数字だけにしろ")
            return # continue and break can only be used inside of a loop so use is used for ending the method/action
        
        amount = int(amount)
        if not self.current_user.withdraw_process(amount): 
        # call the withdraw_process in User class to check if the amount matches the conditions or not
            print("残高が足りない")
            return # same as the return used above
        else:
            print(f"残高：{self.current_user.balance}") # getting user balance from current_user(can be accessed to "self."") object 
            
    def deposit_request(self):
        amount = input("預かり入れ金額を入力：").strip().replace(" ","")
        if not amount.isdigit():
            print("数字だけにしろ")
            return
        
        amount = int(amount)
        new_balance = self.current_user.deposit_process(amount)
        print(f"残高：{new_balance}")
        
    def show_balance(self):
        print(f"残高：{self.current_user.balance}")
        
if __name__ == "__main__":
    user = User("1234", 1000000)
    atm = ATM(user)
    atm.input_pin()
    while True:
        choice = int(input("引き出し(1)？預かり入れ？(2)？残高表示(3)："))
        
        if choice == 1:
            atm.withdraw_request()
            break
        elif choice == 2:
            atm.deposit_request()
            break  
        elif choice == 3:
            atm.show_balance()
            break
        else:
            print("1から3にしろボケ")
            continue