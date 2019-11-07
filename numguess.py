from random import randint


answer = randint(1, 100+1)
print(answer)
print('Hi, welcome to guess game. You can do 3 times.')
chance = 0
while chance < 4:
  guess = int(input('Guess the num(1~100)> '))
  chance = chance + 1
  if guess == answer:
    print("Correct!")
    break
  else:
    print("Wrong!")
