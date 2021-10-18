# 請設計一程式，輸入兩整數M和N (0<M<1000; 0<N<1000)，並計算兩數的
# GCD(可以整除兩數的最大數字)跟LCM(可以被兩數整除的最小數字)。
# (請上GcdLcm.py檔) 

M = int(input("輸入M:"))
N = int(input("輸入N:"))

def c(M,N):
    while(N):
        M,N = N,M%N
    return M
    
def d(M,N):
    return M*N // c(M,N)


print(c(M,N))
print(d(M,N))
