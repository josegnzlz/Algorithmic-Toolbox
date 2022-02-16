# Uses python3
import sys

def optimal_weight(W, w):
    # write your code here
    value = []
    for i in range(0, len(w)+1):
        array = list(0 for j in range(0, W+1))
        value.append(array)
    for i in range(0, len(w)):
        for x in range(1, W+1):
            value[i+1][x] = value[i][x]
            if w[i] >= x and value[i][x-w[i]] + w[i] <= W:
                val = value[i][x-w[i]] + w[i]
                if value[i+1][x] < val:
                    value[i+1][x] = val
    print(value)
    return value[len(w)][W]

if __name__ == '__main__':
    inp = input()
    W, n = map(int,inp.split())
    second = input()
    w = list(map(int, second.split()))
    print(optimal_weight(W, w))
