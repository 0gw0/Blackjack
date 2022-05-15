from art import logo
import random
import os

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

# cards and their value
cards = {'a': 11, "2": 2, "3":3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, 'J': 10, 'Q': 10, 'K': 10}

def calculate_score(list):
  total = 0
  for i in list:
    total += cards[i]
  if total > 21:
    if "a" in list:
      total -= 10
  # if still above 21 change all ace to value 1
  if total > 21 and 'a' in list:
    total += 10
    for i in list:
      if i == 'a':
        total -= 10
  return total

# function to draw first two cards
def starting_hand():
  hand = []
  for i in range(2):
    hand.append(random.choice(list(cards)))
  return hand

def start_game():
  clear()
  print(logo)
  #hands and scores
  computer_hand = starting_hand()
  user_hand = starting_hand()
  user_score = calculate_score(user_hand)
  computer_score = calculate_score(computer_hand)

  # shows coms first card and ur current score
  print (f'Your cards: {user_hand}, current score: {user_score}')
  print (f"Computer's first card: {computer_hand[0]}")

  #while loop that exists when 'n' or when BAO
  play_on = True
  while (play_on):
    if (input('Draw another card? type y/n: ') == 'n'):
      play_on = False
    else:
      user_hand.append(random.choice(list(cards)))
      user_score = calculate_score(user_hand)
      print (f'\nYour cards: {user_hand}, current score: {user_score}')
      if user_score > 21:
        play_on = False
        
  #if com_score < 17 it draws
  while computer_score < 17:
    computer_hand.append(random.choice(list(cards)))
    computer_score = calculate_score(computer_hand)

  #clears, shows everyones cards and winner
  clear ()
  print (logo)
  print (f'Your cards: {user_hand}, final score: {user_score}')
  print (f"Computer's final hand: {computer_hand}, score: {computer_score}")
  # determining who is the winner
  if user_score > 21:
    print("You went over 21, You lose")
  # user loses even if computer BAOs due to house rules
  elif computer_score > 21:
    print("The dealer went over 21, You win!!")
  elif (user_score > computer_score):
    print("You win")
  elif (user_score == computer_score):
    print("Its a draw")
  else:
    print("You lose")

  if(input("Play another game? type y/n: ").lower() == 'y'):
    start_game()

if (input("Do you want to play a game of Blackjack? type 'y' or 'n': ").lower() == 'y'):
  start_game()
else:
  print("Maybe another time then.")
