# Enter your code here. Read input from STDIN. Print output to STDOUT
def calc(N):
    N=2**N
    sum=0
    while N>0:
        sum=sum+N%10
        N=N/10
    return sum    
T=int(raw_input().strip())
while T:
    N=int(raw_input().strip())
    print calc(N)
    T=T-1
