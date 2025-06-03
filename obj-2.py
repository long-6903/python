class player(): # holding players' info and pars list
    def __init__(self, name, score):
        self.pa = [4, 4, 3, 4, 5, 4, 5, 3, 4, 4, 3, 4, 5, 4, 3, 4, 5, 4]
        self.name = name
        self.score = score
                
    def calc_score(self): # 
        # modify line 11 and pass the list pa and name, score in order to use this func in game class
        total_diff = score_diff = 0
        for i in range(len(self.pa)):
            score_diff = self.score[i] - self.pa[i]
            total_diff += score_diff 
        return total_diff
        
class game(): # manage input/ output
    def info_input(self):
        while True:
            first_input = input("入力： ").strip()
            
            if first_input == "":
                print("空入力された")
                continue
            
            last_input = first_input.replace(" ", "").split(",")
            
            if len(last_input) != 38:
                print(f"最初の名前の2つを除いて入力した数：{len(last_input)}")
                print("３８個までちゃんと入れろ")
                continue
            
            p1_name = last_input[0]
            p2_name = last_input[1]
            
            for char in last_input[2:38]:
                if not char.isdigit():
                    print(f"入力不可能{char}が入ってる")
                    break
                num = int(char)
                if num < 0:
                    print("0 < input pls")
                    break
            else:
                p1_score = list(map(int, last_input[2:20])) # splitting and saving parts of input string into player score accordingly
                p2_score = list(map(int, last_input[20:38])) # splitting and saving parts of input string into player score accordingly
                self.player1 = player(p1_name, p1_score) # creating player1 objects
                self.player2 = player(p2_name, p2_score) # creating player2 objects
                break

    def show_result(self):
        p1_result = self.player1.calc_score() 
        p2_result = self.player2.calc_score()
        # 2 lines above : accessing the players(object)' infos which created at line 45,46
        
        print(f"player 1 score : {self.player1.score}"+f"\nThe result is +{p1_result}") # Use score attributes from the player objects
        print(f"player 2 score : {self.player2.score}"+f"\nThe result is +{p2_result}") # Use score attributes from the player objects
        
        if p1_result > p2_result:
            print("player 1 win")
        elif p1_result < p2_result:
            print("player 2 win")
        else:
            print("draw")
            
if __name__ == "__main__":
    golf = game()
    golf.info_input()
    golf.show_result()
    
    
#まとめ 
# 