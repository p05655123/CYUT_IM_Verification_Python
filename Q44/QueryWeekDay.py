# 試撰寫一 Java 程式，可提供使用者查詢一星期中每一日的英文單字
# (Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday)，若輸入的內容非
# 星期一至星期日的範圍，則須顯示"查無此日"的訊息。(請上傳
# QueryWeekDay.py 檔) 

d = str(input("輸入日期:"))

if d == "1":
    print("Monday")
elif  d == "2":
    print("Tuesday")
elif  d == "3":
    print("Wednesday")
elif  d == "4":
    print("Thursday")
elif  d == "5":
    print("Friday")
elif  d == "6":
    print("Saturday")
elif  d == "7":
    print("Sunday")
else:
    print("查無此日")
