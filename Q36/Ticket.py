# 假設電影票的總類與票價如下表:
#     類別   票價(元)
# 1   半票    110
# 2   全票    220
# 3   軍警    180
# 請撰寫程式，輸入電影票的總類M以及購買張數N，並計算出其總金額。(請上傳Ticket.py檔)

m = int(input("輸入類別:"))
n = int(input("輸入張數:"))
s = 0
if m == 1:
    s = 110 * n
    print(s)
elif m == 2:
    s = 220 * n
    print(s)
elif m == 3:
    s = 180 * n
    print(s)