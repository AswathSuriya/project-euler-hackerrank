# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
def nCr(n,r):
    x=1
    for i in range(1,r+1):
        x=x*n
        x=x/i
        n=n-1        
    return int(x)
T=int(raw_input().strip())
while T:
    N,M=map(int,raw_input().split())    
    #print (nCr(500,500))
    print (int(nCr(N+M,M))%(10**9+7))
    T=T-1
