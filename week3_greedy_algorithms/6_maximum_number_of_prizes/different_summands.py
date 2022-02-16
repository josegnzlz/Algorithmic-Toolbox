# Uses python3
import sys

def optimal_summands(n):
    summands = []
    num = n
    sec = 1
    while num > 0:
        if (num <= 2 * sec):
            summands.append(num)
            num = 0
        else:
            summands.append(sec)
            num -= sec
        sec += 1   

    return summands

if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
