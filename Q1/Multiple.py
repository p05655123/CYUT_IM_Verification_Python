# 請試撰寫一程式，讓使用者傳入一數值A，判斷此數是否為2或3的倍數，
# 如是印出true，否則印false。(請上傳Multiple.py檔)
A = int(input('請輸入一數值：'))
if (A%2 == 0) or (A%3 == 0): #判斷是否是2「或」三的倍數
    print('true')
else:
    print('false')

#注意點：看清楚題目，是「或」
#　　　　可用「|」或是「or」