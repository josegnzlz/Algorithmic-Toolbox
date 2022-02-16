# Uses python3
def get_change(m):
    # cuantas monedas se devuelven
    coins = 0
    while m > 0:
        if m >= 10:
            m -= 10
            coins += 1
        elif m >= 5:
            m -= 5
            coins += 1
        else:
            coins += m
            m = 0
    return coins

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
