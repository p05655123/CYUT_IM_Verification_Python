# 請撰寫一程式，輸入N位學生的姓名後，利用排序法依照姓名長度由大到小
# 排序。（請上傳NameSort.py）

n = input("輸入學生姓名 :")
st=n.split(',')

stt = sorted(st,key = lambda i:len(i),reverse=True)

for i in range(len(stt)):
    print(stt[i],end=' ')