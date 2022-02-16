from random import randrange

def swap(a, first, second):
    """ Se intercambian dos posiciones en una lista """
    # print(a)
    # print(f"Posiciones a intercambiar: {first}, {second}")
    # print(f"Correspondientes a: {a[first]}, {a[second]}")
    if first == second:
        return a
    num = a[first]
    a[first] = a[second]
    a[second] = num
    return a

def partition(a, l, r, n_reps):
    """ Se realiza una separación en tres intervalos de la lista """
    # print(f"Comienza la partition de {l} a {r}")
    pivot = a[l]
    pivot_end = l
    minors_end = l
    for i in range(l+1, r):
        """ Se estudian las demas posiciones y se comparan con el pivot """
        if a[i] == pivot:
            minors_end += 1
            pivot_end += 1
            # print(f"1. El final del pivot es: {pivot_end}, el de los minors: {minors_end}, i: {i}, numero estudiado: {a[i]}")
            a = swap(a, minors_end, i)
            # print(a)
            # print(f"2. El final del pivot es: {pivot_end}, el de los minors: {minors_end}, i: {i}, numero estudiado: {a[i]}")
            a = swap(a, pivot_end, minors_end)
            # print(a)
        elif a[i] < pivot:
            minors_end += 1
            # print(f"El final del pivot es: {pivot_end}, el de los minors: {minors_end}, i: {i}, numero estudiado: {a[i]}")
            a = swap(a, minors_end, i)
            # print(a)
    
    reps = pivot_end-l+1
    n_reps.append([pivot, reps])
    last_change_pos = minors_end
    first_change_pos = minors_end - reps + 1 # Si 6 es pivot, 1 2 4 6 6 6 8 9 10; (3,5)

    for x in range(l,l+reps):
        a = swap(a, minors_end, pivot_end)
        minors_end -= 1
        pivot_end -= 1
    # print(f"Al final de la partition el resultado es:")
    # print(a)
    # print(n_reps)
    # print(f"Posicion primera: {first_change_pos}, última: {last_change_pos}")
    return a, n_reps, first_change_pos, last_change_pos

def randomizedQuickSort(a, l, r, n_reps):
    """ Se ordena la lista dada """
    # print(f"Randomized Quick Sort con left: {l} y right: {r}")
    if l >= r:
        return a, n_reps
    
    k = l + randrange(r - l)
    a = swap(a, l, k)
    a, n_reps, p1, p2 = partition(a, l, r, n_reps)

    a, n_reps = randomizedQuickSort(a, l, p1, n_reps)
    a, n_reps = randomizedQuickSort(a, p2 + 1, r, n_reps)

    return a, n_reps

def get_majority_element(a,left,right):
    if left==right or left+1==right:
        return -1
    n_reps = []
    a, n_reps = randomizedQuickSort(a,left,right, n_reps)
    # print(a)
    # print(n_reps)
    major_number = None

    for numbers in n_reps:
        if numbers[1] > right/2:
            major_number = numbers[0]
            return major_number
    return -1

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
