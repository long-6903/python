class game:
    def __init__(self):
        self.pa = [4, 4, 3, 4, 5, 4, 5, 3, 4, 4, 3, 4, 5, 4, 3, 4, 5, 4]
        self.user_score = []

    def score_input(self):
        while True: # inputを繰り返す
            first_input = input("入力：").strip() #delete space and enter of the top and bottom of the input
            
            if first_input == "":
                print("空入力された")
                continue # 空入力されたら、処理を繰り返す / continue : その回の処理をスキップし、次のループへ進む(breakはその回で処理を終わらせる)
            
            space_delete = first_input.replace(" ", "")  # 半角スペースは読み飛ばす
            last_input = space_delete.split(",") # 半角ス   ペースを消したら「,」で区切る
        
            last_score = []
            
            for hantei_char in last_input:
                if not hantei_char.isdigit(): 
                    print(f"invalid character{hantei_char}が入っています。入力可能な文字は、「数字(0-9)」、「カンマ(,)」「半角スペース」のみ")
                    break # 文字でなければbreakしてwhile loopに戻って入力処理を繰り返す
                num = int(hantei_char)
                if num < 0 or num > 9:
                    print("0 以下の整数。もう一回入力")
                    break # 0 以下の整数が入力された場合は、その旨を通知して、再度入力が可能
                last_score.append(num)
            else:
                self.user_score = last_score[:18] # last_scoreでscoreを入れてから18個目で終わらせて、self.user_scoreに代入する
                #　slef.user_scoreに代入した理由：so that i can end last_score at 18th number and then use the self object to do the next step         
                break # breakしないと入力処理が止まらん
            
    def cal_result(self):
        total = 0
        for i in range(len(self.user_score)):
            point_dif = self.user_score[i] - self.pa[i]
            total += point_dif
        return total
    
    def show_result(self):
        score = self.cal_result()
        if len(self.user_score) < 18:
            print(f"{len(self.user_score)}ボールで終了して、")
            print(f"＋{score}")
        else:
            print(f"{len(self.user_score)}ボールで終了して、")
            print(f"＋{score}です。")

if __name__ == "__main__":
    golf = game()
    golf.score_input()
    golf.show_result()