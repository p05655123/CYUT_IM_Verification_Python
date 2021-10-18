# 我們都知道一年有四季，分別是春夏秋冬，請寫一個程式判斷輸入(month)
# 的農曆月數是什麼季節， 1 到 3 月為春天， 4 到 6 月為夏天， 7 到 9 月為
# 秋天， 10 到 12 月為冬天。(請上傳SeasonCheck.py檔) 

n = int(input("請輸入月份 :"))

if (n >= 1 and n <= 3 ):
    print("春天")
elif (n >= 4 and n <= 6 ):
    print("夏天")
elif (n >= 7 and n <= 9 ):
    print("秋天")
elif (n >= 10 and n <= 12 ):
    print("冬天")    