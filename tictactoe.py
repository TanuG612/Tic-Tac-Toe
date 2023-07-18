def printboard(board):
   print(f" { board[0] } | { board[1] } | { board[2] } ")
   print(f"---|---|---")
   print(f" { board[3] } | { board[4] } | { board[5] } ")
   print(f"---|---|---")
   print(f" { board[6] } | { board[7] } | { board[8] } ")

def calboard(board,i,val):
    if board[0]==val and board[1]==val and board[2]==val:
        return 1
    elif board[3]==val and board[4]==val and board[5]==val:
        return 1
    elif board[6]==val and board[7]==val and board[8]==val:
        return 1
    elif board[0]==val and board[4]==val and board[8]==val:
        return 1
    elif board[2]==val and board[4]==val and board[6]==val:
        return 1
    elif board[1]==val and board[4]==val and board[7]==val:
        return 1
    elif board[0]==val and board[3]==val and board[6]==val:
        return 1
    elif board[2]==val and board[5]==val and board[8]==val:
        return 1
    else:
         return 0

#board=['*','*','*','*','*','*','*','*','*']
board=list(range(9))
printboard(board)
turn="X"
i=0
res=0
while i<=8:

    if turn=='X':
            val=int(input("Enter place for X "))
            if board[val]!='X' or board[val]!='O':
              board[val]=turn
              i+=1
              turn="O"
              printboard(board)
              res=calboard(board,i,'X')
              if res==1:
                print("X WINS\nMatch over")
                break
            else:
                print("Already occupied. Please enter again")

    elif turn=="O":
            val=int(input("Enter place for O "))
            if board[val]!='X' or board[val]!='O':
                   board[val]=turn
                   i+=1
                   printboard(board)
                   turn="X"
                   res=calboard(board,i,'O')
                   if res==1:
                      print("O WINS\nMatch over")
                      break
            else:
                 print("Already occupied. Please enter again")
    else:
       print("INVALID INPUT")
if res==0:
     print("Draw\nMatch over")

