import random

answer = random.randint(1, 100)  # 1から100までの整数
attempts = 0

print("1から100までの数字を当ててください！")

while True:
    guess_str = input("数字を入力してください！")

    # 入力が数字かどうかをチェック
    if not guess_str.isdigit():
        print("数字を入力してください！")
        continue
    
    # 文字列を整数に変換
    guess = int(guess_str)
    attempts += 1
    
    # 答えと入力された数字を比較
    if guess == answer:
        print(f"正解！{attempts}回目で当たりました！")
        break
    elif guess < answer:
        print("もっと大きい数字です！")
    else: # guess > answer
        print("もっと小さい数字です！")