# 輸入整數n，試寫程式計算下列級數的值  (請上傳Pseries.py檔)
# sum = 21+22+23+…+2n

sum = 0
n = int(input("輸入整數n："))
for i in range(1,n+1):  
    sum = sum + 2 ** i
print(sum)