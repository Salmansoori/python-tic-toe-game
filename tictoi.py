board=[" " for i in range(9)]
def play_game():
   row1="|{}|{}|{}|".format(board[0],board[1],board[2])
   row2="|{}|{}|{}|".format(board[3],board[4],board[5])    
   row3="|{}|{}|{}|".format(board[6],board[7],board[8])

   print()
   print(row1)
   print(row2)
   print(row3)
   print()
def player(icon):
    if icon=="x":
        number=1
    elif icon=="o":
        number=2
    print("your turn player{}".format(number))    
    choice=int(input("enter choice btw 1-9:").strip()) 
    if board[choice-1]==" ":
       board[choice-1]=icon
    else:
        print()
        print("this space is taken")
def iswon(icon):
    if (board[0]==icon and board[1]==icon and board[2]==icon)or\
        (board[3]==icon and board[4]==icon and board[5]==icon)or\
        (board[6]==icon and board[7]==icon and board[8]==icon)or\
        (board[0]==icon and board[3]==icon and board[6]==icon)or\
        (board[1]==icon and board[4]==icon and board[7]==icon)or\
        (board[2]==icon and board[5]==icon and board[8]==icon)or\
        (board[0]==icon and board[4]==icon and board[8]==icon)or\
        (board[2]==icon and board[4]==icon and board[6]==icon):
        return True
    else:
        False
def draw():
    if " " not in board:
        return True
    else:
        False           
while True:
    play_game()
    player("x")
    play_game()
    if iswon("x"):
        print("x wins!")
        break
    elif draw():
        print("its draw")
        break    
    player("o")
    if iswon("o"):
        play_game()
        print("o wins!")
        break
    elif draw():
        print("its draw")
        break            
