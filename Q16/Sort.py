# 給一堆數字, 把他們從小到大排序好。輸入說明：有n個整數（n≤1000），
# 皆於-10000到10000 之間。輸出說明：輸出已排序好的數列，每個數字之間
# 請用一個空白隔開。(請上傳Sort.py檔)

s=input("輸入n個整數：")
ss=s.split(',')
n=len(ss)
for i in range(n):
    ss[i]=int(ss[i])
ss=sorted(ss)
a=ss[0]
for j in range (1,len(ss)):
    a = str(a) + " " + str(ss[j])
print(a)