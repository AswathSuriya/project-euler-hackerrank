import math as m
def sumseries(a,d,n):
    return (n*(2*a+(n-1)*d))//2

T=int(input())
while T:
    N=int(input())
    N=N-1
    three=m.floor(N/3)
    five=m.floor(N/5)
    fifteen=m.floor(N/15)
    #print(three,five,fifteen)
    print(sumseries(3,3,three)+sumseries(5,5,five)-sumseries(15,15,fifteen))
    T-=1
