class GolfScore:
    def __init__(self): #self is the current object u working with, used to saved infos of the object u working with
        # 各ホールのパー（固定）
        self.pars = [4, 4, 3, 4, 5, 4, 5, 3, 4, 4, 3, 4, 5, 4, 3, 4, 5, 4]
        self.user_scores = []

    def input_scores(self):
        while True:
            raw_input = input("スコアをカンマ(,)区切りで入力してください（例：4,5,3）>> ").strip()
            # ユーザーから入力を受け取る。.strip()で前後のスペースや改行を削除する。

            if raw_input == "":
                print("空の入力です。もう一度入力してください。")
                continue
            # 空入力だったらエラーメッセージを出してやり直し

            cleaned_input = raw_input.replace(" ", "")  # user　inputの中身のspaceを消す
            tokens = cleaned_input.split(",") # spaceを排除した文字列を「,」で区切りする

            valid_scores = [] # 最終scoreの配列

            for token in tokens:
                if not token.isdigit(): #tokens(spaceと改行を消した配列) - token(その配列の数値) 
                    print(f"無効な文字 '{token}' が含まれています。数字とカンマのみ使用できます。   ")
                    break
                num = int(token) # turns token which is a char type shit to int type shit(num)
                if num <= 0 or num > 9:
                    print("0以下か9以上のスコアは無効です。正の整数を入力してください。")
                    break
                valid_scores.append(num) 
            else:
                self.user_scores = valid_scores[:18]  # 19個目以降は無視
                break  # 正常に入力できたら終了

    def calculate_score(self):
        total = 0
        for i in range(len(self.user_scores)):
            total += self.user_scores[i] - self.pars[i]
        return total

    def show_result(self):
        played_holes = len(self.user_scores)
        score_diff = self.calculate_score()
        print(f"{played_holes}ホールプレイしました。")
        print(f"スコア（パーとの差の合計）：{score_diff}")


if __name__ == "__main__":
    game = GolfScore()
    game.input_scores()
    game.show_result()
