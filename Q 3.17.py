import random
choices = ["scissors", "rock", "paper"]
while True:
  try: 
    user_choice = int(input("scissor(0), rock(1), paper(2) quit(3): "))
    if user_choice == 3:
            print("Thanks for playing. Exiting the game.")
            break
    user_choice_str = choices[user_choice]
  except (IndexError ,ValueError):
      print("Wrong input try again")
      continue
  randchoice = random.randint(0,2)
  rand_choice_str = choices[randchoice]
  if user_choice > randchoice :
      print(f"The computer is {rand_choice_str}.You are {user_choice_str}.you lose")
  elif randchoice < user_choice:
      print(f"The computer is {rand_choice_str}.You are {user_choice_str}.You win")
  else:
      print(f"Computer is {rand_choice_str} and you are {user_choice_str}.Its a draw.")
      




