import random

easy_words = ["apple", "train", "tiger", "money", "india"]
mediam_words = ["python", "bottle", "money", "planet", "laptop"]
hard_words = ["elephant", "diamond", "umbrella", "computer", "mountain"]

print("Welcome to the password guessing game")
print("choose your dificulty: easy, medium, hard")

level = input("Enter difficulty : ").lower()
if level == "easy":
    secret = random.choice(easy_words)
elif level == "mediam":
    secret = random.choice(mediam_words)
elif level == "hard":
    secret = random.choice(hard_words)
else :
    print("Invalid Choice!, Defaulting to easy level")
    secret = random.choice(easy_words)
attempts= 0
while True:
    guess = input("Enter your guess :").lower()
    attempts += 1

    if(guess == secret):
        print(f"Congretulations! You geussed it in {attempts} attempts")
        break

    hint = ""
    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint += guess[i]
        else:
            hint+="_"

    print("Hint : ", hint)

print("Game Over") 
