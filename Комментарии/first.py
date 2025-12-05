import random

secret_number = random.randint(1, 5)

attempts = 0
max_attempts = 3

print("Я загадал число от 1 до 5")
print("У тебя есть", max_attempts, "попытки")

while attempts < max_attempts:
    guess = int(input("Введи число: "))
    
    if guess == secret_number:
        print("Ура! Ты угадал!")
        break
    elif guess < secret_number:
        print("Больше!")
    else:
        print("Меньше!")
    
    attempts = attempts + 1
    
    if attempts < max_attempts:
        print("Осталось попыток:", max_attempts - attempts)

if attempts == max_attempts:
    print("Попытки закончились. Было число:", secret_number)
