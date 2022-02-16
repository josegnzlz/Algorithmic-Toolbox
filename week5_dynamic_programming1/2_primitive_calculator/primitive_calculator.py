# Uses python3       

def optimal_sequence(n):
    compendium = []
    compendium.append([n])
    sequence = []
    index = None
    if n == 1:
        sequence.append(1)
        return sequence
    if n == 2:
        sequence.append(1)
        sequence.append(2)
        return sequence
    if n == 3:
        sequence.append(1)
        sequence.append(3)
        return sequence
    results = [n-1]
    operations = [1]
    if n % 2 == 0:
        results.append(int(n/2))
        operations.append(2)
    if n % 3 == 0:
        results.append(int(n/3))
        operations.append(3)
    compendium.append(operations)
    compendium.append(results)
    # print(compendium)
    while True:
        results, operations = [], []
        for x in compendium[-1]:
            # print(f"Estudiando el numero: {x}")
            results.append(x - 1)
            operations.append(1)
            if x % 2 == 0:
                # print("Divisible entre 2")
                results.append(int(x/2))
                operations.append(int(2))
            if x % 3 == 0:
                # print("Divisible entre 3")
                results.append(int(x/3))
                operations.append(int(3))
        compendium.append(operations)
        compendium.append(results)
        # print(operations)
        # print(results)
        try:
            results.index(1)
        except ValueError:
            pass
        else:
            break

    # print(compendium)

    index = compendium[len(compendium)-1].index(1)
    for i in reversed(range(0,len(compendium),2)):
        sequence.append(compendium[i][index])
        count = 0
        for j in range(0,index):
            if compendium[i-1][j] == 1:
                count += 1
        index = count - 1
    return sequence


n = int(input())
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
