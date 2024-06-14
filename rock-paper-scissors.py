from random import randint;

print("Rock!\nPapers!\nScissors!\n")

valid_choices = ['rock', 'paper', 'scissors'];
random_computer_pick = valid_choices[randint(0,2)]

player = input("Player please enter your choice: ").lower()

computer_wins = f"I chose {random_computer_pick} so I win! :D"
player_wins = f"I chose {random_computer_pick} so you win! D:"
tie = f"I chose {random_computer_pick} so it's a tie :|"

if player:
  if player not in valid_choices:
    print(f"Please enter a valid choice: {valid_choices}")
  elif random_computer_pick == player:
    print(tie)
  elif random_computer_pick == 'rock':
    if player == 'scissors':
      print(computer_wins)
    else:
      print(player_wins)
  elif random_computer_pick == 'paper':
    if player == 'rock':
      print(computer_wins)
    else:
      print(player_wins)
  elif random_computer_pick == 'scissors':
    if player == 'paper':
      print(computer_wins)
    else:
      print(player_wins)