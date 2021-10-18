# 給一個偶數n，請你將n 分解成兩個質數的和，也就是說，這兩個質數
# 相加的和必須等於n。輸入說明：輸入一個數字，數字的範圍為[4, 10000]
# 間的偶數。輸出說明：對輸入的每筆測試資料，分別輸出 2 個質數，用一
# 個空白做為區隔，請由小到大排列(以第一個找到的符合的答案為主)。


def month(x):
    return{
    1:31,
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31,
    }.get(x,'error')
    


s = str(input('請輸入年份及月份:'))
ss=s.split(',')
y = int(ss[0])
m = int(ss[1])

if m > 12 | m < 1:
    print('您輸入的資料有誤')
elif m == 2 :
    if (y % 4 == 0) & (y % 100 != 0) | (y % 400 == 0):
        print('29')
    else :
        print('28')
else :
    print(month(m))
    

