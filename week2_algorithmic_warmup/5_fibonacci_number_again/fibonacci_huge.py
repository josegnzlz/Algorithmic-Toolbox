# Uses python3
import sys
## Quiero conocer el period

def calc_fib(n):
    fib = []
    fib.append(0)
    fib.append(1)
    for i in range(2,n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib[n]

def get_fibonacci_huge(n, m):
    if n <= 1:
        return n

    period = [0, 1]
    active = True
    x = 2

    while active:
        fib_number = calc_fib(x)
        fib_mod = fib_number % m
        if fib_mod == period[1] and period[-1] == period[0]:
            active = False
            period.pop()
        else:
            period.append(fib_mod)
            x += 1
    
    act_n = n % len(period)
    return period[act_n]
        

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(get_fibonacci_huge(n, m))
