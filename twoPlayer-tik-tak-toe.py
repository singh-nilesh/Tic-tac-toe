# Following is Terminal based Tik-tac-toe game

import os

# Display grid
def printGrid(arr):
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(2,9,3):
        print(f"  {arr[i-2]}  |  {arr[i-1]}  |  {arr[i]}")
        if(i < 6):
            print("________________")


#Check Grid
def checkGrid(arr):
    # check rows
    for i in range(2,9,3):
        if(arr[i] == arr[i-1] and arr[i-1] == arr[i-2] and arr[i] != ' '):
            print("\n ",arr[i], " wins !!!")
            return True
    
    # check Column
    for i in range(3):
        if(arr[i] == arr[i+3] and arr[i+3] == arr[i+6] and arr[i] != ' '):
            print("\n ",arr[i], " wins !!!")
            return True
    
    # check diagonal 1 (init + row_len + 1)
    if(arr[0] == arr[4] and arr[4] == arr[8] and arr[0] != ' '):
        print("\n ",arr[0], " wins !!!")
        return True
    
    # check diagonal 2 (init + row_len - 1)
    if(arr[2] == arr[4] and arr[4] == arr[6] and arr[2] != ' '):
        print("\n ",arr[2], " wins !!!")
        return True
    
    # Check draw    
    end = False
    for val in arr:
        if (val != ' '):
            end = True
        else:
            end = False
            break
    if(end):print("\n DRAW \t game over.")

    return end


# Player Input
def getInput(arr,plr):

    try:
        index = int(input(f"\n player( {plr} )'s move: "))
    except ValueError:
        print("\n Enter only numbers")
        return getInput(arr,plr)
    
    # fill the values
    if((index >= 0 and index <= 8) and arr[index] == ' ' ):
        arr[index] = plr
        return arr
    else:
        print("\t Incorrect move")
        return getInput(arr,plr)



# main Implimentation
end = False
array = [i for i in range(9)]
print(printGrid(array),"\n plese enter the index (0 to 8) \n ")

array = [' ' for i in range(9)]
while (end is False):
    # player 1 round
    array = getInput(array,'X')
    printGrid(array)
    end = checkGrid(array)

    if(end):break

    #player 2 round
    array = getInput(array,'O')
    printGrid(array)
    end = checkGrid(array)