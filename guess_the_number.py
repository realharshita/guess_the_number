import random

def generate_random_number():
    return random.randint(1, 100)

def get_user_guess():
    guess = int(input("Enter your guess: "))
    return guess

def provide_feedback(guess, target):
    if guess < target:
        print("Too low!")
    elif guess > target:
        print("Too high!")
    else:
        print("Correct!")

def play_game():
    target = generate_random_number()
    guess_count = 0
    while True:
        guess = get_user_guess()
        guess_count += 1
        provide_feedback(guess, target)
        if guess == target:
            break
    print(f"Congratulations! You guessed the number in {guess_count} tries.")

def main():
    print("Welcome to the Guess the Number Game!")
    play_game()

if __name__ == "__main__":
    main()
