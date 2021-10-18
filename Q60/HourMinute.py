# 請撰寫一個程式可由鍵盤輸入時間(小時、分鐘)，然後在螢幕上顯示出對應的
# 時鐘上分針與時針之間的夾角為幾度。(請上傳HourMinute.py檔) 

h = int(input("輸入小時:"))
m = int(input("輸入分鐘:"))

o = abs((30*h)-(5.5*m))

if (o > 180):
    o = 360 - o
    print(o)
else:
    print(o)