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
    
    def withdraw_request(self, withdrawAmount):
        if withdrawAmount > self.balance:
            return False
        else:
            self.balance -= withdrawAmount
            return True
            
    def deposit_request(self, depositAmount):
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

    def withdraw_process(self):
        amount = input("引き出す金額を入力：").strip().replace(" ","")
        if not amount.isdigit():
            print("数字だけにしろ")
            return
        
        amount = int(amount)
        if not self.current_user.withdraw_request(amount):
            print("残高が足りない")
            return
        else:
            print(f"残高：{self.current_user.balance}")
            
    def deposit_process(self):
        amount = input("預かり入れ金額を入力：").strip().replace(" ","")
        if not amount.isdigit():
            print("数字だけにしろ")
            return
        
        amount = int(amount)
        new_balance = self.current_user.deposit_request(amount)
        print(f"残高：{new_balance}")
        
    def show_balance(self):
        print(f"残高：{self.current_user.balance}")
        
if __name__ == "__main__":
    user = User("1234", 1000000)
    atm = ATM(user)
    atm.input_pin()
    for choice in range(1,3):
        choice = int(input("引き出し(1)？預かり入れ？(2)？残高表示(3)："))
        
        if choice == 1:
            atm.withdraw_process()
            break
        elif choice == 2:
            atm.deposit_process()
            break  
        elif choice == 3:
            atm.show_balance()
            break
        else:
            print("1から3にしろボケ")
            continue