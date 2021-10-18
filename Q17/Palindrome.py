# 迴文是指某個子串的正向拼法和逆向拼法都相同。撰寫一個遞迴方法，
# 傳入一佪字串(text)，如其為迴文則印出”true”，否則印出”false”。 
# (請上傳Palindrome.py檔)

s = str(input("輸入一段字串："))
a = s[::-1]
if s == a :
    print("ture")
else:
    print("false")