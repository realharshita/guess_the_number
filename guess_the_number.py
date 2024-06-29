import tkinter as tk
import random

class GuessNumberGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Guess the Number Game")

        self.label = tk.Label(root, text="Welcome to the Guess the Number Game!")
        self.label.pack()

        self.difficulty_label = tk.Label(root, text="Select difficulty level: easy, medium, hard")
        self.difficulty_label.pack()

        self.difficulty_entry = tk.Entry(root)
        self.difficulty_entry.pack()

        self.guess_label = tk.Label(root, text="")
        self.guess_label.pack()

        self.guess_entry = tk.Entry(root)
        self.guess_entry.pack()

        self.feedback_label = tk.Label(root, text="")
        self.feedback_label.pack()

        self.score_label = tk.Label(root, text="")
        self.score_label.pack()

        self.target = None
        self.guess_count = 0

    def start_game(self):
        difficulty = self.difficulty_entry.get().lower()
        self.target = self.generate_random_number(difficulty)
        self.guess_count = 0
        self.guess_label.config(text="Enter your guess:")
        self.feedback_label.config(text="")
        self.score_label.config(text="")

    def generate_random_number(self, difficulty):
        if difficulty == 'easy':
            return random.randint(1, 10)
        elif difficulty == 'medium':
            return random.randint(1, 100)
        elif difficulty == 'hard':
            return random.randint(1, 1000)
        else:
            self.feedback_label.config(text="Invalid difficulty level")
            return None

    def submit_guess(self):
        guess = int(self.guess_entry.get())
        self.guess_count += 1
        self.provide_feedback(guess)

    def provide_feedback(self, guess):
        if guess < self.target:
            self.feedback_label.config(text="Too low!")
        elif guess > self.target:
            self.feedback_label.config(text="Too high!")
        else:
            self.feedback_label.config(text="Correct!")
            self.display_score()

    def display_score(self):
        score = max(100 - self.guess_count, 0)
        self.score_label.config(text=f"Congratulations! You guessed the number in {self.guess_count} tries.\nYour score: {score}")

def main():
    root = tk.Tk()
    game = GuessNumberGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
