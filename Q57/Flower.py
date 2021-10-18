# 鬱金香一朵50元、香水百合一朵10元、白玫瑰一朵5元、滿天星一朵1元，
# 現有一筆金額N (0<100)，請設計一程式，計算出此金額若全部用完，能買
# 到的最少花朵數。輸入說明：輸入金額n。輸出說明：第一個數為花朵總數。
# 第二個到第五個分別為鬱金香、香水百合、白玫瑰、滿天星的花朵數。
# (每一個數中間隔一格空格) (請上傳Flower.py檔)

a,a1,a2,a3,a4 = 0 ,0,0,0,0
money=int(input("輸入金額:"))
if (money >= 50):
    a1 = money //50
    money = money -(a1 * 50)

if (money >= 10):
    a2 = money // 10
    money = money -(a2 *10)

if (money >= 5):
    a3 = money // 5
    money = money -(a3 * 5)

if (money >= 1):
    a4 = money // 1
    money = money -(a4*1)
a = a1+a2+a3+a4
print(a,a1,a2,a3,a4)
