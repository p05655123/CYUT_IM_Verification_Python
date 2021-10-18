# 以下為常用的兩種日期格式 4/25/1955 和 April 25,1955 ，撰寫一個程
# 式，能夠讀入第一種格式的日期字串(dateStr)， 並以第二種格式列印出來。
# ( 月份英文： January, February , March, April, May, June, July, August,
# September, October, November, December ； 請上傳 DateTranslate.py 檔 )

def month(x):
    return{
        "1" : "January",
        "2" : "February",
        "3": "March",
        "4": "April",
        "5" : "May",
        "6" : "June",
        "7": "July",
        "8": "August",
        "9": "September",
        "10" : "October",
        "11": "November",
        "12" : "December",

    }.get(x,'error')


day=input("輸入日期:")
d=day.split('/')
print(month(d[0]), d[1] + ","+d[2])