import random

while True:
    number = random.randint(1,100)
    attempts = 0
    print("\n New Game Started!")

    while True:
        guess = int(input("Guess a number between 1 and 100: "))
    
        attempts += 1
        
        if guess == number:
            print(f"correct! You guessed it in {attempts}attempts.")
            break
        elif guess < number:
            print("too low")
        else:
            print("too high")

            again = input("Do you want to play again?(yes/no): ")
            if again.lower() != "yes":
                print("GAME OVER")
                break
