# 現在有n個蛋，一打是12 個，請設計java程式, 輸入一個整數n, 計算此n個蛋
# 是幾打，還剩下幾個蛋。（請上傳Egg.py）

n = int(input("輸入n:"))
d = 0
b = 0
d = n // 12
b = n % 12
print(d,b)
