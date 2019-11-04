# Rock Paper Scissor Game
# Program to play Rock Paper Scissor Game with Computer

from random import randint
  
player = input('Rock (r) , Paper (p) , Scissorr (s) : ')

if(player == 'r'):
  print('Rock', end=' ')
  
elif(player == 'p'):
  print('Paper', end=' ')
  
elif(player == 's'):
  print('Scissor', end=' ')
  
else:
  print('???')
  
print('vs', end=' ')

chosen = randint(1,3)

if(chosen == 1):
  computer = 'r'
  print('Rock')
  
elif(chosen == 2):
  computer = 'p'
  print('Paper')
  
else:
  computer = 's'
  print('Scissor')

if(player == computer):
  print('DRAW!')
  
elif(player == 'r' and computer == 's'):
  print('Player Wins!')
  
elif(player == 'r' and computer == 'p'):
  print('Computer Wins!')
  
elif(player == 'p' and computer == 'r'):
  print('Player Wins!')
  
elif(player == 'p' and computer == 's'):
  print('Computer Wins!')

elif(player == 's' and computer == 'p'):
  print('Player Wins!')
  
elif(player == "s" and computer == 'r'):
  print('Computer Wins!')

else:
  print('Try Again!!!')
