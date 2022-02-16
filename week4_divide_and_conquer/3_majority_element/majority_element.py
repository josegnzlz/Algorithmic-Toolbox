# Uses python3
from math import floor
from random import random, randrange

def swap(array, first_index, second_index):
    if(first_index == second_index):
        return a
    num = array[first_index]
    try:
        k = array[second_index]
    except:
        print(f"Excepción, índice que ha dado el fallo: {second_index}")
    array[first_index] = k
    array[second_index] = num
    return a

def partition(array, l, r):
    init = l
    end_part = l
    end_less = l
    number = array[l]
    # print("Dentro de PARTITION")
    # print(array)
    print(f"Left: {l}, Right: {r}")
    for x in range(l+1, r):
        # print(f"El valor de x en este paso es: {x}")
        if array[x] == array[l]:
            end_part += 1
            end_less += 1
            print(f"La end part es: {end_part}, y la x: {x}")
            array = swap(a, end_part, x)
        if array[x] < array[l]:
            end_less += 1
            print(f"La x es: {x}, y la end less es: {end_less}")
            array = swap(a, x, end_less)
    dif = end_part - init
    for w in range(init, end_part+1):
        array = swap(a, w, end_less)
        end_less -= 1
    
    return [array, end_less+1, end_less+1+dif, number]


def randomizedQuickSort(a, left, right, n_reps):
    if right<=left:
        return a, n_reps
    #write your code here
    # print(f"El valor de right es {right}, el de left es {left}, la diferencia es: {right-left}")
    rand_index = left+randrange(right-left)
    a = swap(a, left, rand_index)
    # print("Antes de PARTITION")
    # print(a)

    [a, part_index1, part_index2, number] = partition(a, left, right)
    n_reps.append([number, part_index2-part_index1+1])
    # print(f"Tras PARTITION: {part_index1}, {part_index2}")
    # print(a)
    # print(n_reps)
    a, n_reps = randomizedQuickSort(a, left, part_index1, n_reps)
    a, n_reps = randomizedQuickSort(a, part_index2+1, right, n_reps)

    return a, n_reps

def get_majority_element(a,left,right):
    if left==right or left+1==right:
        return -1
    n_reps = []
    a, n_reps = randomizedQuickSort(a,left,right, n_reps)
    print("#" * 50)
    print(a)
    print(n_reps)
    maj_number = None
    reps = 0
    for i in range(0, len(n_reps)):
        if n_reps[i][1] > reps:
            maj_number = n_reps[i][0]
            reps = n_reps[i][1]
        elif n_reps[i][1] == reps:
            return -1

    if reps/len(a) > 0.5:
        return maj_number
    else:
        return -1



if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
