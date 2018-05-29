#Ask the user what size of game board do they want to print?
board_size=int(input("What is the size of the game board?"))
def board():
  print(" ---"*board_size)
  print("|   "*(board_size+1))
for x in range(board_size):
  board()
print(" ---"*board_size)
