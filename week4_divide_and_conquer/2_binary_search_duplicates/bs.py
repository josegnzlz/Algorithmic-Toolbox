from math import floor

def binary_search(keys, b):
    i = 0
    j = len(keys) - 1
    res = -1

    while True:
        # print(f"El límite inferior en este paso es {i}")
        # print(f"El límite superior en este paso es {j}")
            
        index = i + floor((j-i)/2)
        middle = keys[index]
        # print(f"El número middle es {middle}")

        if j < i:
            break

        if b == middle:
            res = index
            # print(f"Se ha encontrado el resultado, al menos de primeras, es {index}")
            j = index -1
        elif b > middle:
            i = index + 1
        elif b < middle: # Esto no funciona para el caso en el que se esten analizando solo dos numeros ya
            j = index - 1
        
    return res


if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for b in input_queries:
        print(binary_search(input_keys, b), end=' ')