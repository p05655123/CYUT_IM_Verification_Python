# 撰寫一個程式，讀入9個整數至陣列data，請利用迴圈及陣列，撰寫一程式
# 計算這些整數的中間值。(請上傳Middle.py檔)

s=input("請輸入9個整數：")
ss=s.split(',')
n=len(ss)
for i in range(n):
    ss[i]=int(ss[i])
ss=sorted(ss)
print(ss[4])