import random

def win(arr):
  # check in rows
  for i in arr:
    if i == ['O','O', 'O']:
      print('Player O has won the game!')
      return True
    elif i == ['X', 'X', 'X']:
      print('Player X has won the game!')
      return True
  #check in columns
  for i in range(3):
    if arr[0][i] == 'O' and arr[1][i] == 'O' and arr[2][i] == 'O':
      print('Player O has won the game!')
      return True
    elif arr[0][i] == 'X' and arr[1][i] == 'X' and arr[2][i] == 'X':
      print('Player X has won the game!')
      return True
  #check across
  if arr[0][0] == 'O' and arr[1][1] == 'O' and arr[2][2] == 'O':
    print('Player O has won the game!')
    return True
  elif arr[0][0] == 'X' and arr[1][1] == 'X' and arr[2][2] == 'X':
    print('Player X has won the game!')
    return True
  elif arr[0][2] == 'O' and arr[1][1] == 'O' and arr[2][0] == 'O':
    print('Player O has won the game!')
    return True
  elif arr[0][0] == 'X' and arr[1][1] == 'X' and arr[2][0] == 'X':
    print('Player X has won the game!')
    return True
  return False
  
def board(arr):
  print('\n')
  for i in arr:
    print('|'.join(i))
  print('\n')
  
def replace(move):
  if (move / 3) <= 1:
    place = my_arr[0][move-1]
    if place != ' ':
      print('There is already an X or a O in that space\n')
      return False
    my_arr[0][move-1] = turn
  elif (move / 3) <= 2:
    place = my_arr[1][move-4]
    if place != ' ':
      print('There is already an X or a O in that space\n')
      return False
    my_arr[1][move-4] = turn
  else:
    place = my_arr[2][move-7]
    if place != ' ':
      print('There is already an X or a O in that space\n')
      return False
    my_arr[2][move-7] = turn
    

my_arr = [ [' ',' ',' '], [' ',' ',' '], [' ',' ',' '] ]
print('This is the numbers corresponding the spaces\n')
print("1|2|3\n4|5|6\n7|8|9\n")

turn = 'X'
counter = 0

while True:
  user_move = input(f'{turn} player\'s turn. what is your move? ')
  if not user_move.isnumeric():
    print('You must enter a number!')
  if int(user_move) <= 9:
    if replace(int(user_move)) is False:
      continue
  board(my_arr)
  counter += 1
  if win(my_arr):
    break
  elif counter == 9:
    print('It\'s a tie!')
    break
  elif turn == 'X':
    turn = 'O'  
  else:
    turn = 'X'
