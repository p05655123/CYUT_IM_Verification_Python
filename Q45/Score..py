# 讀入一個學生的作業成績(homework)、期中考成績(middleExam)、以及期未
# 考成績(finalExam)。如果學生的期末考成績達 70 分 ( 含 ) 以上印出及格，
# 或作業成績 80 分 ( 含 ) 以上且期中考成績不低於 60 分，也印出 "及格
# " ，其他則印出 "不及格"。 ( 請上傳 Score.py 檔 )


a=int(input("輸入作業成績:"))
b=int(input("輸入期中考成績:"))
c=int(input("輸入期末考成績:"))

if (c >= 70) or ((a >= 80) and b > 60):
    print("及格")
else:
    print("不及格")
