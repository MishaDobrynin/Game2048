from move import moveUp, moveLeft, moveDown, moveRight, emptyField
import os
from random import choice
from termcolor import colored

# https://github.com/shiena/ansicolor/blob/master/README.md
# Array that contains the value of numbers
arr = [[" ", " ", " ", " "],
       [" ", " ", " ", " "],
       [" ", " ", " ", " "],
       [" ", " ", " ", " "]
       ]
blank = [["||       |", "|       |", "|       |", "|       ||"],
         ["||       |", "|       |", "|       |", "|       ||"],
         ["||       |", "|       |", "|       |", "|       ||"],
         ["||       |", "|       |", "|       |", "|       ||"]
         ]
blank2 = [["||       |", "|       |", "|       |", "|       ||"],
          ["||       |", "|       |", "|       |", "|       ||"],
          ["||       |", "|       |", "|       |", "|       ||"],
          ["||       |", "|       |", "|       |", "|       ||"]
          ]

colors = {
    "2": "on_red",
    "4": "on_green",
    "8": "on_yellow",
    "16": "on_blue",
    "32": "on_magenta",
    "64": "on_cyan",
    "128": "on_red",
    "256": "on_green",
    "512": "on_yellow",
    "1024": "on_blue",
    "2048": "on_magenta"
}

gameRunning = True
was2048 = False


def gameField():
    global blank
    print("--------------------------------------")
    for i in range(len(arr)):
        middle = ["|" + el.center(7) + "|" for el in arr[i]]
        for x in range(len(arr[i])):
            if arr[i][x] != " ":
                blank[i][x] = [colored(" ", "grey", colors[arr[i][x]]) if el == " " else el for el in blank[i][x]]
                blank[i][x] = "".join(blank[i][x])

        for x in range(4):
            if checkDigit(middle[x]):
                middle[x] = "".join([colored(" ", "grey", colors[arr[i][x]]) if el == " " else colored(el, "white",
                                                                                                       colors[arr[i][
                                                                                                           x]]) if el.isdigit() else el
                                     for el in middle[x]])
        print("".join(blank[i]))
        print("|" + "".join(middle) + "|")
        print("".join(blank[i]))
        print("--------------------------------------")

        for x in range(4):
            blank[i][x] = blank2[i][x]


def addRandomTile():
    global arr
    possible = choice(emptyField(arr))
    mark = choice(["2", "2", "2", "2", "2", "2", "2", "2", "2", "4"])
    arr[possible[0]][possible[1]] = mark


def checkInput():
    global arr
    key = input()
    while key not in ["w", "a", "s", "d"]:
        key = input()
    if key == "w":
        for i in range(len(arr)):
            for x in range(len(arr[i])):
                if arr[i][x] != " ":
                    arr[i][x] = int(arr[i][x])
                else:
                    arr[i][x] = 0
        arr = moveUp(arr)
        for i in range(len(arr)):
            arr[i] = [str(el) if el != 0 else " " for el in arr[i]]
    elif key == "a":
        for i in range(len(arr)):
            arr[i] = moveLeft([int(el) if el != " " else 0 for el in arr[i]])
            arr[i] = [str(el) if el != 0 else " " for el in arr[i]]
    elif key == "s":
        for i in range(len(arr)):
            for x in range(len(arr[i])):
                if arr[i][x] != " ":
                    arr[i][x] = int(arr[i][x])
                else:
                    arr[i][x] = 0
        arr = moveDown(arr)
        for i in range(len(arr)):
            arr[i] = [str(el) if el != 0 else " " for el in arr[i]]
    elif key == "d":
        for i in range(len(arr)):
            arr[i] = moveRight([int(el) if el != " " else 0 for el in arr[i]])
            arr[i] = [str(el) if el != 0 else " " for el in arr[i]]

def clearBoard():
    os.system("clear")

def checkDigit(arr):
    for el in arr:
        if el.isdigit():
            return True
    return False


addRandomTile()
addRandomTile()

while gameRunning:
    clearBoard()

    gameField()

    checkInput()
    try:
        addRandomTile()
    except:
        break
print("You lost!")