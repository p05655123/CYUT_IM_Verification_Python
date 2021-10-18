# 全台灣有2500萬人左右，而每個人對其他人都有一個喜好的程度，如
# 果這些喜好程度可以排成一等差數列，那我們就說愛有等差。輸入說明 ：
# 每一行有n個數字Ki (-10000＜Ki＜10000)，代表這位路人對n個人分別
# 的喜好程度。輸出說明 ：如果愛有等差，就輸出YES，不然輸出NO。(記
# 得先排序)(請上傳Sequence.py檔)


s=input('請輸入一串數字:')
ss=s.split(',')
n=len(ss)
for i in range(n):
    ss[i]=int(ss[i])

ss=sorted(ss)  #數字排序(從小到大)

for i in range(n-2):
    if (ss[i+1] - ss[i])==(ss[i+2] - ss[i+1]) :
        flag = 1
    else:
        flag = 0
        break

if flag == 1:
    print('YES')
else :
    print('NO')