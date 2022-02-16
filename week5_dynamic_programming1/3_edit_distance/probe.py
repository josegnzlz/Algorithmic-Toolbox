d = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for u in range(1,3):
    d[0][u] = d[0][u-1] + 1
    print(d[0][u])
for y in range(1,3):
    d[y][0] = d[y-1][0] + 5
    print(d[y][0])

for k in d:
    print(k)