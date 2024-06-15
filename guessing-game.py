from random import randint

random_number = randint(0,9)
guess = None

while random_number != guess:
  guess = int(input('Guess a digit between 0 and 9: '))
  if random_number > guess:
    print('Too low! guess again..')
  elif random_number < guess:
    print('Too high, guess again..')  
  else:
    print("You guessed it!")
    play_again = input('Do you waint to play again? (y/n) ')
    if play_again == 'y':
      random_number = randint(0,9)
      guess = None
    else:
      print('Thank you for playing!')
      break