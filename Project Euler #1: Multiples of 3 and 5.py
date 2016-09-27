'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below .

Input Format
First line contains that denotes the number of test cases. This is followed by lines, each containing an integer, .

Output Format
For each test case, print an integer that denotes the sum of all the multiples of or below .

Sample Input
2
10
100

Sample Output
23
2318

Explanation
For N = 10, if we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Similarly for N = 100, we get 2318.
'''
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
