from string import ascii_uppercase

coordinates = [
    [20, 18], [21, 12], [16, 31],
    [27, 27], [25, 11], [32, 15],
    [16, 6], [33, 8], [18,5]
]

offset = [
    [0, 0], [45, 0], [90, 0],
    [0, 45], [45, 45], [90, 45],
    [0, 90], [45, 90], [90, 90]
]

for i in range(9):
    x = coordinates[i][0] + offset[i][0]
    y = coordinates[i][1] + offset[i][1]

    x %= 26
    y %= 26

    x = ascii_uppercase[x]
    y = ascii_uppercase[y]

    print(y)
    print(x)
