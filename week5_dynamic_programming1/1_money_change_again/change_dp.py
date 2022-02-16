# Uses python3
import sys

def get_change(m):
    coins = [4, 3, 1]
    min_num_coins = []
    min_num_coins.append(0)
    for i in range(1, m+1):
        min_num_coins.append(10000)
        for coin in coins:
            if i >= coin:
                num_coins = min_num_coins[i-coin]+1
                if num_coins < min_num_coins[i]:
                    min_num_coins[i] = num_coins
    
    return min_num_coins[m]

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
