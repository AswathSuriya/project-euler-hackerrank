A=[]
for i in range(20):
    a=[int(x) for x in input().strip().split(' ')]
    A.append(a)
sum=0
#horizontal
for i in range(20):
    for j in range(17):
        s=A[i][j]*A[i][j+1]*A[i][j+2]*A[i][j+3]
        if s>sum:
            sum=s
#vertical
for i in range(17):
    for j in range(20):
        s=A[i][j]*A[i+1][j]*A[i+2][j]*A[i+3][j]
        if s>sum:
            sum=s
#forward diagonal
for i in range(17):
    for j in range(17):
        s=A[i][j]*A[i+1][j+1]*A[i+2][j+2]*A[i+3][j+3]
        if s>sum:
            sum=s
#backward diagonal
for i in range(17):
    for j in range(3,20):
        #print(i,j)
        #print(A[17][4])
        s=A[i][j]*A[i+1][j-1]*A[i+2][j-2]*A[i+3][j-3]
        if s>sum:
            sum=s
print(sum)
