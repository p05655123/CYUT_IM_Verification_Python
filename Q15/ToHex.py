# 撰寫一個程式，可以將0到255十進位的數目(N)，轉換成等值的十六進制的數。
# (請上傳ToHex.py檔)

n=int(input("輸入N："))
a=hex(n)
a=a[2:]
a=a.upper() #轉大寫
print(a)
