# 在三位數的正整數中，比如說一整數N，其個位數十位數百位數分別以c、
# b、a，Armstrong數則可以滿足a3 + b3 + c3 = abc的條件，也就是說，各個
# 位數的立方和正好是該數的本身，這些數就叫做Armstrong數。設計一
# 程式輸入整數N判斷一個三位數是否為Armstrong數。(請上傳 Armstrong.py)

n = int(input("輸入n:"))
c = str(n)
b = list(c)
a1 = int(b[0])
a2 = int(b[1])
a3 = int(b[2])
z = (a1**3) + (a2**3) + (a3**3)
if z == n:
    print("true")
else:
    print("false")