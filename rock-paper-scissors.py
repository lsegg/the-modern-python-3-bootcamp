from random import randint

print("Rock!\nPapers!\nScissors!\n(Best out of 3)\n")
valid_choices = ['rock', 'paper', 'scissors']
computer_score = 0
player_score = 0

def computer_wins(pick):
  print(f"I chose {pick} so I win! :D")
  global computer_score
  computer_score = computer_score + 1
  
def player_wins(pick):
  print (f"I chose {pick} so you win! D:")
  global player_score
  player_score = player_score + 1

for time in range(3):
  print(f'Current score:\n you ({player_score}) vs me({computer_score})')
  random_computer_pick = valid_choices[randint(0,2)]
  player = input("Player please enter your choice: ").lower()

  if player:
    if player == 'quit':
      break
    if player not in valid_choices:
      print(f"Please enter a valid choice: {valid_choices}")
    elif random_computer_pick == player:
      print(f"I chose {random_computer_pick} so it's a tie :|")
    elif random_computer_pick == 'rock':
      if player == 'scissors':
        computer_wins(random_computer_pick)
      else:
        player_wins(random_computer_pick)
    elif random_computer_pick == 'paper':
      if player == 'rock':
        computer_wins(random_computer_pick)
      else:
        player_wins(random_computer_pick)
    elif random_computer_pick == 'scissors':
      if player == 'paper':
        computer_wins(random_computer_pick)
      else:
        player_wins(random_computer_pick)

print(f'Final score:\n you ({player_score}) vs me({computer_score})')