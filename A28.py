print ("TIC TAC TOE board. Rows and Columns starting from 1,1")
print ("Game board is printed each time to show progress!")
# Declare the blank game           
game=[[0,0,0], 
      [0,0,0],
      [0,0,0]]
count = 0
# create the print gameboard function
def print_game(game):
    print ("\n")
    for i in range(3):
        print (str(game[i]) + "\n")
# Insert the checkWin function here.
def check():
  if game[0][0]==game[1][0]==game[2][0]:
    if game[0][0]=='X':
      print("Player 1 wins")
      breakgame=1
    elif game[0][0]=='O':
      print("Player 2 wins")
      breakgame=1
  elif game[0][1]==game[1][1]==game[2][1]:
    if game[0][1]=='X':
      print("Player 1 wins")
      breakgame=1
    elif game[0][1]=='O':
      print("Player 2 wins")
      breakgame=1
  elif game[0][2]==game[1][2]==game[2][2]:
    if game[0][2]=='X':
      print("Player 1 wins")
      breakgame=1
    elif game[0][2]=='O':
      print("Player 2 wins")
      breakgame=1
  elif game[0][0]==game[0][1]==game[0][2]:
    if game[0][0]=='X':
      print("Player 1 wins")
      breakgame=1
    elif game[0][0]=='O':
      print("Player 2 wins")
      breakgame=1
  elif game[1][0]==game[1][1]==game[1][2]:
    if game[1][0]=='X':
      print("Player 1 wins")
      breakgame=1
    elif game[1][0]=='O':
      print("Player 2 wins")
      breakgame=1
  elif game[2][0]==game[2][1]==game[2][2]:
    if game[2][0]=='X':
      print("Player 1 wins")
      breakgame=1
    elif game[2][0]=='O':
      print("Player 2 wins")
      breakgame=1
  elif game[0][0]==game[1][1]==game[2][2]:
    if game[0][0]=='X':
      print("Player 1 wins")
      breakgame=1
    elif game[0][0]=='O':
      print("Player 2 wins")
      breakgame=1
  elif game[0][2]==game[1][1]==game[2][0]:
    if game[0][2]=='X':
      print("Player 1 wins")
      breakgame=1
    elif game[0][2]=='O':
      print("Player 2 wins")
      breakgame=1
  else:
    print("tie")
# Now lets start the game
while True:
  #Insert the code from the statement.
  spot = input("Enter the row,column in same format as given: ")
  spot = spot.split(",") # This will remove the comma
  row = int(spot[0]) -1    
  column = int(spot[1]) -1
  if count%2==0:
   print ("\nPlayer 1's Turn!")
   if game[row][column] == 0:  # Make sure the spot is blank
     game[row][column] = 'X'   # if it's blank, mark an X
     count+=1
     check()
   else:
     print ("Try Again!")      # if it's not blank, try again
     count-=1   # this will reset the counter, so you can try again
   print_game(game)  # print your new game board
        
  else:
        # Now do the same thing for player 2 as you did for player 1
        # Player 2 is an 'O'
    print ("\nPlayer 2's Turn!")    
    if game[row][column] == 0:  # Make sure the spot is blank
      game[row][column] = 'O'   # if it's blank, mark an X
      check()
    else:
      print ("Try Again!")      # if it's not blank, try again
      count-=1   # this will reset the counter, so you can try again
    print_game(game)  # print your new game board
    #Increase your count
    count+=1
    #check for a win using your function that you created
    check()

print ("Game Over!")
