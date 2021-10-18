# 請設計一個程式，能在一個數列中，找出相鄰兩數的最小距離。輸入
# 說明：每個數字與數字間的區隔為一個空白符號。輸入範圍：每個數列
# 最少有2個數字，最多不超過100個。每個數列中的數字皆大於0，小於1000，
# 且不重覆。（請上傳MinDist.py）

s=input("輸入數列:")
ss=s.split(',')
n=len(ss)
for i in range(n):
    ss[i]=int(ss[i])

a = abs(ss[1] - ss[0])
for j in range(n-1):
    
    if a > abs(ss[j+1] - ss[j]):
        a = abs(ss[j+1] - ss[j])

print(a)
