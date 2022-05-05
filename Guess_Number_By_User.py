
import random
random_number = random.randint(1, 10)
#print(random_number)
guess = 0
while guess != random_number:
    guess = int(input(f'Guess a number between 1 and 9: '))
    if guess < random_number:
        print('Sorry, guess again. Too low.')
    elif guess > random_number:
        print('Sorry, guess again. Too high.')

print(f'Yay, congrats. You have guessed the number {random_number} correctly!!')

