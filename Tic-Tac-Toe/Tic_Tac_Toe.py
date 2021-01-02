#-----GLOBAL VARIABLES-----

#game board
board=["-","-","-",
      "-","-","-",
      "-","-","-"]

#If game is still going
game_still_going=True

#Who won? or tie?
winner=None

#Whose turn is this
current_player="X"

#display board
def display_board():

  print(board[0]+"|"+board[1]+"|"+board[2])
  print(board[3]+"|"+board[4]+"|"+board[5])
  print(board[6]+"|"+board[7]+"|"+board[8])

#handle the turn of an arbitrary player 
def handle_turn(player):
  print(player+"'s Turn.")
  position=input("Choose a number from 1-9: ")

  valid=False
  while not valid:
    while position not in ['1','2','3','4','5','6','7','8','9']:
      position=input("Choose a number from 1-9: ")
    
    position=int(position)-1

    if board[position]=='-':
      valid=True
    else:
      print("You can't go there. Go again.")
  board[position]=player
  display_board()

def check_rows():
  #set global VARIABLES
  global game_still_going
  #check if any of the row has same value but not '-'
  row_1=board[0]==board[1]==board[2]!='-'
  row_2=board[3]==board[4]==board[5]!='-'
  row_3=board[6]==board[7]==board[8]!='-'
  #if any row has a match then state global variable as False
  if row_1 or row_2 or row_3:
    game_still_going=False
  #Return the winner 'X' or 'Y'
  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]
  return

def check_columns():
  #set global VARIABLES
  global game_still_going
  #check if any of the row has same value but not '-'
  column_1=board[0]==board[3]==board[6]!='-'
  column_2=board[1]==board[4]==board[7]!='-'
  column_3=board[2]==board[5]==board[8]!='-'
  #if any row has a match then state global variable as False
  if column_1 or column_2 or column_3:
    game_still_going=False
  #Return the winner 'X' or 'Y'
  if column_1:
    return board[0]
  elif column_2:
    return board[1]
  elif column_3:
    return board[2]
  return

def check_diagonals():
  #set global VARIABLES
  global game_still_going
  #check if any of the row has same value but not '-'
  diagonal_1=board[0]==board[4]==board[8]!='-'
  diagonal_2=board[2]==board[4]==board[6]!='-'
  #if any row has a match then state global variable as False
  if diagonal_1 or diagonal_2:
    game_still_going=False
  #Return the winner 'X' or 'Y'
  if diagonal_1:
    return board[0]
  elif diagonal_2:
    return board[2]
  return

def check_for_winner():
  global winner
  #check rows
  row_winner=check_rows()
  #check columns 
  column_winner=check_columns()
  #check diagonals
  diagonal_winner=check_diagonals()
  if row_winner:
    winner=row_winner
  elif column_winner:
    winner=column_winner
  elif diagonal_winner:
    winner=diagonal_winner
  else:
    winner=None
  return

def check_if_tie():
  #set global variable
  global game_still_going
  if '-' not in board:
    game_still_going=False
  return

def check_if_game_over():
  
  check_for_winner()
  check_if_tie()

def flip_player():
  #set global variable
  global current_player
  #checking if current player is X or O
  if current_player=='X':
    current_player='O'
  elif current_player=='O':
    current_player='X'
  return

#Play a game of tic tac toe
def play_game():

  #display initial board
  display_board()

  #while the game is still going
  while game_still_going:

    #handle the single turn of a player
    handle_turn(current_player)

    #Check if game is over
    check_if_game_over()

    #Fip the turn of player
    flip_player()


#The game has ended
  if winner=='X' or winner=='O':
    print(winner + " won.")
  elif winner==None:
    print("Tie.")

play_game();



#board
#board display
#play game
#handle turn
#check win
  #check row
  #check column
  #check diagonals
#check tie
#flip player
