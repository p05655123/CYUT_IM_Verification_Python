# 讀取一串的文字或數字，將其按數字、大寫英文字母、小寫英文字母排序。
# (請上傳LetterSort.py檔)  

s=str(input("輸入一串文字或數字:"))
a=sorted(s)
for i in a:
    print(i,end="")