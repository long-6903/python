class player:
    def __init__(self, name, score):
        self.pa = [4, 4, 3, 4, 5, 4, 5, 3, 4, 4, 3, 4, 5, 4, 3, 4, 5, 4]
        self.player_name = name
        self.player_score = score
    
    def score_cal(self):
        total = 0
        for i in self.player_score:
            point_diff = self.player_score[i] - self.pa[i]
            total += point_diff
        return total
    
class Game:
    def user_input(self):
        while 1:
            raw_input = input("入力： ").strip().replace(" ","").split(",")
            
            if raw_input == "":
                print("space detected")
                continue
            if len(raw_input) != 38:
                print(f"player pointは{len(raw_input)-2}しか入力されてないので36個まで入力")
                continue
            
            p1_name = raw_input[0]
            p2_name = raw_input[1]
            
            for hantei in raw_input[2:38]:
                if hantei.isdigit() == False:
                    print("数字じゃないのが入っている")
                    break
                num = int(hantei)
                if num < 0:
                    print("負の数字が入ってる")
                    break
                raw_input.append(num)
            else:
                p1_score = list(map(int, raw_input[2:20]))
                p2_score = list(map(int, raw_input[20:38]))
                
                self.p1 = player(p1_name, p1_score)
                self.p2 = player(p2_name, p2_score)
                
                break
              
    def show_result(self):
        p1_result = self.p1.score_cal()
        p2_result = self.p2.score_cal()
        
        print(f"{self.p1.player_name} " + f" {self.p1.player_score}" + f" {p1_result}")
        print(f"{self.p2.player_name} " + f" {self.p2.player_score}" + f" {p2_result}")
        
        if p1_result < p2_result:
            print(f"{self.p1.player_name} win")
        elif p1_result > p2_result:
            print(f"{self.p2.player_name} win")
        else:
            print("draw")
            
wholeGame = Game()
wholeGame.user_input()
wholeGame.show_result()