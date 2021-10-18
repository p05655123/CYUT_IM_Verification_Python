# 請設計一個 Python 程式，輸入一個只以秒為單位的整數(second)，將其換
# 算為以時、分及秒為單位的時間(請上傳 TimeTranslate.py 檔) 

S = int(input("輸入秒:"))


M = S // 60
S = S % 60

H = M // 60
M = M % 60

print( str(H) + "時" + str(M) + "分" + str(S) + "秒")