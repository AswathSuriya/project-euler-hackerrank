# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
def calc(N):    
    N=math.factorial(N)
    sum=0
    while N>0:
        sum=sum+N%10
        N=N/10
    print sum    
T=int(raw_input().strip())
while T:
    N=int(raw_input().strip())
    calc(N)
    T=T-1
