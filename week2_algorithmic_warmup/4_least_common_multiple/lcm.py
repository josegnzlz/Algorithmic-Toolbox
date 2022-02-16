# Uses python3
import sys

def euclid_gcd(a, b):
    if b == 0:
        return a
    a_lemma = a % b
    return euclid_gcd(b, a_lemma)

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(int(a * b / euclid_gcd(a, b)))

