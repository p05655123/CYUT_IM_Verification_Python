# 設計一個程式，能夠輸入一個字串(text)，單字之間以"#"分隔，請將此行文字
# 的單字取出，並以相反的順序輸出。(請上傳Token.py檔)


s = str(input('請輸入一字串以#做分隔'))
ss=s.split('#')
print(ss)
sss=ss[::-1]   #用來倒轉資料
print(sss)
a=sss[0]
for i in range (1,len(sss)):
    a = a + '#' + sss[i]
print(a)