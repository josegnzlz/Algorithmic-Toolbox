# Uses python3
def edit_distance(word1, word2):
    # tengo que crear una matriz de tamaño len(s)+1, len(t)+1
    d = []
    
    for w in range(0, len(word2)+1):
        arr = []
        for x in range(0,len(word1)+1):
            if w == 0:
                if x == 0:
                    arr.append(0)
                else:
                    arr.append(x)
            else:
                if x == 0:
                    arr.append(w)
                else:
                    arr.append(0)
        d.append(arr)

    # for k in d:
    #     print(k)
    # print("#")

    for i in range(1, len(word2)+1):
        for j in range(1, len(word1)+1):
            # print(f"Fila {i}, Columna {j}")
            insertion = d[i][j-1] + 1
            deletion = d[i-1][j] + 1
            match = d[i-1][j-1]
            mismatch = d[i-1][j-1] + 1

            if word1[j-1] == word2[i-1]:
                d[i][j] = min(insertion, deletion, match)
            else:
                d[i][j] = min(insertion, deletion, mismatch)
    # for k in d:
    #     print(k)
    # print("#")
    return d[len(word2)][len(word1)]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
