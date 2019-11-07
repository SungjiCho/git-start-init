from random import randint


answer = randint(1, 100+1)
print(answer)
print('Hi, welcome to guess game. You can do 3 times.')

def compare_guess():
  chance = 3
  for _ in range(chance):
    guess = int(input('Guess the num(1~100)> '))
    chance = chance + 1
    if guess == answer:
      print("Correct!")
      break
    else:
      print("Wrong!")

compare_guess()
