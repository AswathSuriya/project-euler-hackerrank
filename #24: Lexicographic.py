import math

T=int(input())
while T:
    s = ['a','b','c','d','e','f','g','h','i','j','k','l','m',]
    N=int(input())
    N-=1
    f = math.factorial(12)
    d = 12
    while d!=0:
        #print(N,f)
        index = N//f
        N=N%f
        print (s[index], end='')
        s.remove(s[index])
        f//=d
        d-=1
    print (s[0])
    T-=1
