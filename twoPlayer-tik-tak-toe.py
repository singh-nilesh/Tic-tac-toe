# This is a Terminal based Tick-tack-toe game.
import os

def printGrid(matrix):
    os.system('cls' if os.name == 'nt' else 'clear')
    for i,row in enumerate(matrix):
        print(f"  {row[0]}  |  {row[1]}  |  {row[2]}")
        if(i != len(matrix)-1):
            print("________________")


def checkGrid(matrix):
    # check rows
    for row in matrix:
        if(row[0] == row[1] and row[1] == row[2] and row[2] != ' '):
            print("\n ",row[0], " wins !!!")
            return True
    
    # check Column
    for i in range(3):
        col_list = []
        for j in range(3):
            col_list.append(matrix[j][i])
        
        if (col_list[0] == col_list[1] and col_list[1] == col_list[2] and col_list[2] != ' '):
            print("\n ",col_list[0], " wins !!!")
            return True
    
    # check diagonals
    if(matrix[0][0] == matrix[1][1] and matrix[1][1] == matrix[2][2] and matrix[1][1] != ' '):
        print("\n ",matrix[0][0], " wins !!!")
        return True
    
    if(matrix[0][2] == matrix[1][1] and matrix[1][1] == matrix[2][0] and matrix[1][1] != ' '):
        print("\n ",matrix[0][2], " wins !!!")
        return True
    
    # Check draw    
    end = False
    for row in matrix:
        if (' ' not in row):
            end = True
        else:
            end = False
            break
    if(end):print("\n DRAW \t game over.")

    return end


# player 1 input
def getInput_X(matrix):
    
    p1 = int(input(f"\n player( X )'s move: "))    
    i = (p1 - p1%3)// 3
    j = p1%3

    if((p1 >= 0 and p1 <= 8) and matrix[i][j] == ' ' ):
        matrix[i][j] = 'X'
        return matrix
    else:
        print("\t Incorrect move")
        return getInput_X(matrix)

#player 2 input
def getInput_O(matrix):

    p1 = int(input(f"\n player( O )'s move: "))   
    i = (p1 - p1%3)// 3
    j = p1%3

    if((p1 >= 0 and p1 <= 8) and matrix[i][j] == ' ' ):
        matrix[i][j] = 'O'
        return matrix
    else:
        print("\t Incorrect move")
        return getInput_O(matrix)



# main Implimentation
end = False
matrix = [[' ' for i in range(3)] for col in range(3) ]

print("plese enter the index (0 to 8) \n ",printGrid(matrix))
while (end is False):
    # player 1 round
    matrix = getInput_X(matrix)
    printGrid(matrix)
    end = checkGrid(matrix)

    if(end):break

    #player 2 round
    matrix = getInput_O(matrix)
    printGrid(matrix)
    end = checkGrid(matrix)