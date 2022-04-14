import random

no_of_player = int(input("Enter the number of players : "))
i = 1
score = []
players = []

while i <= no_of_player:
    correct_number = random.randint(1, 100)
    name = input("Enter your name : ")
    no_of_guess = 0
    while True:
        guess = int(input("Enter your guess : "))

        if guess > correct_number:
            no_of_guess += 1
            print(f"Please guess lower than {guess}.")

        elif guess < correct_number:
            no_of_guess += 1
            print(f"Please guess higher than {guess}")

        else:
            print("Congrulations! You have guessed the correct number!")
            break

    print(f"You have guessed the number in {no_of_guess} trails.")
    score.append(no_of_guess)
    players.append(name)
    print(f"Your score is recorded successfully!")
    i += 1

min_score = min(score)
winner = players[score.index(min_score)]
print(f"{winner} is the winner with score {min_score}!")
