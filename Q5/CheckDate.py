# 撰寫一個Java程式，輸入年(year)、月(month)、日(day)三個整數，檢查是否
# 為合法日期，如是則印出此日期(yyyy/mm/dd)，否則印出"日期錯誤"。
# (請上傳CheckDate.py檔 )

def month(x):
    return{
    1: 31,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
    }.get(x,'error')
    
y = int(input('請輸入年：'))
m = int(input('請輸入月：'))
d = int(input('請輸入日：'))

if (m > 12) | (m < 1) | (d < 1):
    print('日期錯誤')
elif m == 2:
    if (y % 4 == 0)&(y % 100 != 0)|(y % 400 == 0):
        if d > 29:
            print('日期錯誤')
        else:
             print(str(y)+'/'+str(m)+'/'+str(d))
    else:
        if d > 28:
            print('日期錯誤')
        else:
             print(str(y)+'/'+str(m)+'/'+str(d))
else:

    if d > month(m):
         print('日期錯誤')
    else:
         print(str(y)+'/'+str(m)+'/'+str(d))
