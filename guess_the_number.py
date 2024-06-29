import random

def generate_random_number(difficulty):
    if difficulty == 'easy':
        return random.randint(1, 10)
    elif difficulty == 'medium':
        return random.randint(1, 100)
    elif difficulty == 'hard':
        return random.randint(1, 1000)
    else:
        print("Invalid difficulty level")
        return None

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

def select_difficulty():
    print("Select difficulty level: easy, medium, hard")
    difficulty = input("Enter difficulty: ").lower()
    return difficulty

def calculate_score(guess_count):
    return max(100 - guess_count, 0)

def play_game():
    difficulty = select_difficulty()
    target = generate_random_number(difficulty)
    if target is None:
        return

    guess_count = 0
    while True:
        guess = get_user_guess()
        guess_count += 1
        provide_feedback(guess, target)
        if guess == target:
            break
    
    score = calculate_score(guess_count)
    print(f"Congratulations! You guessed the number in {guess_count} tries.")
    print(f"Your score: {score}")

def main():
    print("Welcome to the Guess the Number Game!")
    play_game()

if __name__ == "__main__":
    main()
