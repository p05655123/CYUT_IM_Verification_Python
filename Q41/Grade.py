# 撰寫一個 Java 程式，輸入一學生的學期成績(score)，如學生的平均成績在
# 90~100 之間，則印出Ａ，學期成績在 80~89 之間，則印出 B，學期成績在
# 70~79 之間，則印出 C，學期成績在 60~69 之間，則印出 D，要是成績低於
# 60，就印出 E。（請上傳 Grade.py）

s = int(input("輸入成績:"))

if (s >= 90):
    print("A")
elif (s >= 80 and s <= 89):
    print("B")
elif (s >= 70 and s <= 79):
    print("C")
elif (s >= 60 and s <= 69):
    print("D")
else:
    print("E")