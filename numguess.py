from random import randint


answer = randint(1, 100+1)
print(answer)
guess = int(input('Hi, guess the num(1~100)> '))
if answer == guess:
  print("정답입니다!")
else:
  print("오답입니다!")
