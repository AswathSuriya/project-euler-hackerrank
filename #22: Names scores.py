# Enter your code here. Read input from STDIN. Print output to STDOUT
def calc(st):
    value=0
    for i in range(0,len(st)):
        value=value+(ord(st[i])-64)        
    return value
names=[]
N=int(raw_input().strip())
for i in range(0,N):
    names.append(raw_input().strip())
list={}
copy=names
copy.sort()
for i in range(0,N):
    list[copy[i]]=i+1
Q=int(raw_input().strip())
for i in range(0,Q):
    q=raw_input().strip()    
    x=list[q]
    val=calc(q)
    print val*x
