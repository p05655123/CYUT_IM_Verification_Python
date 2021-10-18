# 寫一個程式，輸入一個字串(text)，計算此字串成對字元出現的次數。
# (請上傳Pair.py)

s=input("輸入一個字串：")
a=set(s)
z=0
for i in a:
    z = z+ (s.count(i)//2)
print(z)
