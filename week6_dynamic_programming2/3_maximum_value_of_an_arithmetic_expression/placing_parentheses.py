# Uses python3
def min_and_max(i,j, operations, min_table, max_table):
    minimo = 10000000
    maximo = -10000000
    # Rehacer esto para que no me cuente el segundo termino
    for k in range(i, j):
        m1 = min_table[i][k]
        M1 = max_table[i][k]
        m2 = min_table[k+1][j]
        M2 = max_table[k+1][j]
        a = evalt(M1, M2, operations[k])
        b = evalt(M1, m2, operations[k])
        c = evalt(m1, m2, operations[k])
        d = evalt(m1, M2, operations[k])

        minimo = min(minimo, a, b, c, d)
        maximo = max(maximo, a, b, c, d)
    
    return minimo, maximo

def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def string_comprehension(string):
    lista_num = []
    n = []
    operators = []
    number = ""
    for x in range(0,len(string)):
        # print(string[x])
        if string[x].isnumeric():
            n.append(string[x])
        else:
            number = "".join(n)
            n=[]
            lista_num.append(int(number))
            number=""
            operators.append(string[x])
    if len(n) != 0:
        number = "".join(n)
        n=[]
        lista_num.append(int(number))
    return lista_num, operators

def get_maximum_value(dataset):
    #write your code here
    numbers, operators = string_comprehension(dataset)
    max_table = []
    for i in range(0, len(numbers)): # Inicializando tablas
        array = list(numbers[i] if j == i else 0 for j in range(0,len(numbers)))
        if i + 1 < len(numbers):
            array[i+1] = evalt(numbers[i], numbers[i+1], operators[i])
        max_table.append(array)
    print(max_table)
    min_table = max_table.copy()
    for s in range(2, len(numbers)):
        for i in range(0, len(numbers) - s):
            j = i + s
            min_table[i][j], max_table[i][j] = min_and_max(i,j,operators, min_table, max_table)
            print(max_table)
    return max_table[0][len(numbers)-1]
    # return max_table

if __name__ == "__main__":
    print(get_maximum_value(input()))
