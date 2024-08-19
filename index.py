import random

def guessingGame():

  secret_number = random.randint(1, 100)

  attempts = 0

  print("Guess a number between 1 and 100.")

  while True:
    try:
      guess = int(input("Take a guess: "))
      attempts += 1

      if guess == secret_number:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break
      elif guess < secret_number:
        print("Too low! Try again.")
      else:
        print("Too high! Try again.")
    except ValueError:
      print("Invalid input. Please enter a number.")

guessingGame()
