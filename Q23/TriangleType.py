# 請設計一Java程式，由使用者任意輸入三角形的三邊長 (邊長為整數，且輸入值並未經過大小排
# 列)後，判斷此三邊所組成之三角形是何種三角形 ，並印出答案。(請上傳TriangleType.py檔) 
# 【提示】 假設輸入的三邊長分別為：a， b，c；且 a<=b<=c
# 若 a=b 或 b=c 則為等腰三角形,  a=b=c 則為正三角形,c >= a + b 則為非三角形

a = int(input("輸入a："))
b = int(input("輸入b："))
c = int(input("輸入c："))

if a == b and b == c and c == a:
    print("正三角形")
    
elif a == b or b == c or a == c :
    print("等腰三角形")

elif a + b > c and b + c > a and c + a > b :
    print("一般三角形")

else:
     print("非三角形")