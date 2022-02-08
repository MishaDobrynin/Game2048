def moveUp(arr):
    array = []
    num = []
    for i in range(4):
        lst = []
        for x in range(4):
            lst.append(arr[x][i])

        array.append(moveLeft(lst))

    for i in range(4):
        lst = []
        for x in range(4):
            lst.append(array[x][i])
        num.append(lst)
    return num


def moveLeft(arr):
    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1]:
            arr[i] += arr[i + 1]
            arr[i + 1] = 0
    return [el for el in arr if el != 0] + [0] * arr.count(0)


def moveDown(arr):
    array = []
    num = []
    for i in range(4):
        lst = []
        for x in range(4):
            lst.append(arr[x][i])

        array.append(moveRight(lst))

    for i in range(4):
        lst = []
        for x in range(len(array)):
            lst.append(array[x][i])
        num.append(lst)
    return num


def moveRight(arr):
    arr = arr[::-1]
    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1]:
            arr[i] = arr[i] + arr[i + 1]
            arr[i + 1] = 0
    new = [el for el in arr if el != 0] + [0] * arr.count(0)
    return new[::-1]


def emptyField(arr):
    lst = []
    for i in range(4):
        for x in range(4):
            if arr[i][x] == " ":
                lst.append([i, x])
    return lst