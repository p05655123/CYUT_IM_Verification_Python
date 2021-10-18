# 撰寫一個程式輸入N個學生成績，並輸出其總和與平均。
# （請上傳SumAverage.py）

n =input("輸入N個學生成績:")
g=n.split(',')
a = 0
for i in range(len(g)):
    g[i]=int(g[i])
    a = a + g[i]
b = a / len(g)
print("sum:" + str(a) +" " + "average:" + str(b))