#Uses python3

import sys

def max_dot_product(a, b):
    #write your code here
    res = 0
    if type(a) == int:
        return a*b
    profit = sorted(a, reverse=True)
    clicks = sorted(b, reverse=True)
    res = sum([profit[i] * clicks[i] for i in range(0, len(profit))])
    return res

if __name__ == '__main__':
    n = int(input())
    if n == 1:
        a = int(input())
        b = int(input())
    else:
        a = list(map(int,input().split()))
        b = list(map(int,input().split()))
    print(max_dot_product(a, b))
    
