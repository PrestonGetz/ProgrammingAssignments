game=[[1,2,0],
      [2,1,0],
      [2,1,1]]
if game[0][0]==game[1][0]==game[2][0]:
  if game[0][0]==1:
    print("Player 1 wins")
  elif game[0][0]==2:
    print("Player 2 wins")
elif game[0][1]==game[1][1]==game[2][1]:
  if game[0][1]==1:
    print("Player 1 wins")
  elif game[0][1]==2:
    print("Player 2 wins")
elif game[0][2]==game[1][2]==game[2][2]:
  if game[0][2]==1:
    print("Player 1 wins")
  elif game[0][2]==2:
    print("Player 2 wins")
elif game[0][0]==game[0][1]==game[0][2]:
  if game[0][0]==1:
    print("Player 1 wins")
  elif game[0][0]==2:
    print("Player 2 wins")
elif game[1][0]==game[1][1]==game[1][2]:
  if game[1][0]==1:
    print("Player 1 wins")
  elif game[1][0]==2:
    print("Player 2 wins")
elif game[2][0]==game[2][1]==game[2][2]:
  if game[2][0]==1:
    print("Player 1 wins")
  elif game[2][0]==2:
    print("Player 2 wins")
elif game[0][0]==game[1][1]==game[2][2]:
  if game[0][0]==1:
    print("Player 1 wins")
  elif game[0][0]==2:
    print("Player 2 wins")
elif game[0][2]==game[1][1]==game[2][0]:
  if game[0][2]==1:
    print("Player 1 wins")
  elif game[0][2]==2:
    print("Player 2 wins")
else:
  print("tie")
