# 請定義四季的中英文名稱對照關係，當輸入英文可以翻譯為中文，當輸入
# 中文可以翻譯為英文（春天:spring, 夏天:summer,　秋天:fall, 冬天:winter）
# （請上傳SeasonName.py）

s=str(input("輸入季節:"))
if s == "春天":
    print("spring")
elif  s == "spring":
    print("春天")
elif  s == "夏天":
    print("summer")
elif  s == "summer":
    print("夏天")
elif  s == "秋天":
    print("fall")
elif  s == "fall":
    print("秋天")
elif  s == "冬天":
    print("winter")
elif  s == "winter":
    print("冬天")
else:
    print("您輸入的資料不符合格式")