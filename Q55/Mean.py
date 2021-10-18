# 試寫一個程式，要求使用者輸入兩個整數a,b，計算這兩個整數的算術平均數
# (a+b)/2與幾何平均數sqrt(a*b)。(請上傳Mean.py檔)

import math
a = int(input("輸入a:"))
b = int(input("輸入b:"))

print(((a+b)/2))
print(math.sqrt(a*b))
print((a*b)**0.5)