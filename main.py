from random import randrange
from time import sleep

def game(start_code):
  intro_sequence(start_code)

  print()
  prt("P1's Turn")
  p1_number = role()

  print()
  prt("P2's Turn")
  p2_number = role()

  announce_winner(p1_number, p2_number)
  end_sequence()

def role():  
  number = 0
  
  for x in range(3):
    prt("A number is drawn")
    number = randrange(1, 12)
    
    answer = ""
    while True:
      answer = input("Rerole? (Yes/y or No/n): ").lower()
      if (answer == "yes" or answer == "y" or answer == "no" or answer == "n"):
        break

    if answer == "yes" or answer == "y":
      number = randrange(1, 12)
    else:
      break
  
  return number

def intro_sequence(start_code):

  if start_code == 1:
    print("-------------------------")
    prt("Welcome back!")
  else:
    prt("Instruction")
    prt("Each player rolls a dice. The number drawn is shown to neither players. She or he may reroll the dice, up to three times, or go on with the number they have. Whoever has a bigger number wins. P1 starts!")

def end_sequence():
  answer = ""
  
  print()
  while True:
    answer = input("Play Again? (Yes/y or No/n): ").lower()
    if (answer == "yes" or answer == "y" or answer == "no" or answer == "n"):
      break

  if answer == "yes" or answer == "y":
    game(1)
  else:
    exit
  

def announce_winner(p1, p2):
  print()
  prt("p1's number: {}".format(p1))
  prt("p2's number: {}".format(p2))
  if p1 > p2:
    prt("p1 wins!")
  elif p2 > p1:
    prt("p2 wins!")
  else:
    prt("Draw")


def prt(s):
  print(s)
  sleep(0.5)
game(0)