import random
board = [["", "", ""], ["", "", ""], ["", "", ""]]



def place(letter,location):
    
    if location <=3:
        if board[0][location-1]== '':
            board[0][location-1] = letter
        else:    
            print("Pick another location")

    elif location > 3 and location<=6 :
        if board[1][location-4] == '':
            board[1][location-4] = letter
        else:    
            print("Pick another location")

    elif location > 6 and location <= 9:
        if board[2][location-7] == '':
            board[2][location-7] = letter
        else:
                print("Pick another location")
    else:
        print("wrong location")

def ai():
    notFilled = []
    for i in range(len(board)):
        for j in range(3):
            if board[i][j] =="":
                notFilled.append([i,j])
    fill = random.choice(notFilled)
    board[fill[0]][fill[1]] = "o"

winner = ""

def isFilled():
    notFilled = []
    for i in range(len(board)):
        for j in range(3):
            if board[i][j] == "":
                notFilled.append([i, j])
    if len(notFilled)==0:
        return True
    else:
        return False            


    
def checkWinner():
    global winner
    # horizontal
    if board[0][0] ==board[0][1]==board[0][2] and board[0][0]!='':
        winner = board[0][0]
        return True
    elif board[1][0] == board[1][1] == board[1][2] and board[1][1] != '':
        winner= board[1][1]
        return True
    elif board[2][0] == board[2][1] == board[2][2] and board[2][2] != '':
        winner = board[2][2]
        return True
    # vertical
    elif board[0][0] == board[1][0] == board[2][0] and board[0][0] != '':
        winner = board[0][0]
        return True
    elif board[0][1] == board[1][1] == board[2][1] and board[0][1] != '':
        winner = board[0][1]
        return True
    elif board[0][2] == board[1][2] == board[2][2] and board[1][2] != '':
        winner = board[1][2]
        return True
    # diagonal
    elif board[0][0] == board[1][1] == board[2][2] and board[0][0] != '':
        winner = board[0][0]
        return True
    elif board[0][2] == board[1][1] == board[2][0] and board[0][1] != '':
        winner = board[0][1]
        return True
    else:
        return False


def printBoard():
    for i in board:
        print(i)


printBoard()
while checkWinner()==False and isFilled() == False:
    ai()
    print("AI PLAYED\n")
    printBoard()
    print("\n")
    place("x",int(input("Pick a valid location from 1-9 :")))

    print("You Played\n")
    printBoard()
    print("\n")

if winner =="x":
    print("YOU WIN !!!")
elif winner =="0":
    print("AI WINS !!!")

   
  
    



                         


                  

