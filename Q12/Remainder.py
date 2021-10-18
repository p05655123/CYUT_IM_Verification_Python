# 求餘數對人來說，是個簡單的問題。但如果算式為R = B^P mod M 的型態，
# 給B、P、及M，要算出餘數R，當B 或P 很大時，那就變得不簡單了。現在，
# 請你設計一個程式，來解決上述這個不簡單的問題。 輸入說明： 每一行包含
# 三個數字，分別為B、P、及M。所有數字均為正整數，其範圍屬於[1,1000]。
# 輸出說明：對輸入的測試資料以一行輸出餘數R。（請上傳Remainder.py檔）



b = int(input("b:"))
p = int(input("p:"))
m = int(input("m:"))

if (b > 1000 or b < 1 ) or (p > 1000 or p < 1)or(m > 1000 or m < 1):
    print("程式錯誤")

# if p > 1000 | p < 1 :
#     print("程式錯誤") 
     
# if m > 1000 | m < 1 :
#     print("程式錯誤")

else:
    R =b** p % m
    print(R)
