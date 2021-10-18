# 撰寫一個程式，輸入一個字串(text)，並將此字串的每個字元重複兩次後印出。
# （請上傳 Repeat.py）

s = input("輸入一字串:")
a = ""
for i in range(len(s)):
    a = a +s[i]+s[i]
print(a)