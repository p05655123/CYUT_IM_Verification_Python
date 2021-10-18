# 請判斷出數列是否為等比數列。輸入說明:每行均包含四個以空白格開的整
# 數，表示數列的前四項。數列的前四項均為不大於10000的自然數。輸出說
# 明:判斷每個數列，是否為等比數列，是請輸出Yes否則輸出No。
# (請上傳Propotion.py檔)

s=input("輸入四個整數：")
ss=s.split(',')
n=len(ss)
for i in range(n):
    ss[i]=float(ss[i])

if ss[0] / ss[1] == ss[1] / ss[2] == ss[2] / ss[3]:
    print("Yes")
else:
    print("No")