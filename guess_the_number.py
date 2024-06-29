import tkinter as tk
import random

class GuessNumberGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Guess the Number Game")
        self.root.configure(bg='lightblue')

        self.label = tk.Label(root, text="Welcome to the Guess the Number Game!", bg='lightblue', fg='black', font=('Helvetica', 16))
        self.label.pack(pady=10)

        self.difficulty_label = tk.Label(root, text="Select difficulty level: easy, medium, hard", bg='lightblue', fg='black', font=('Helvetica', 14))
        self.difficulty_label.pack()

        self.difficulty_entry = tk.Entry(root, font=('Helvetica', 14))
        self.difficulty_entry.pack(pady=5)

        self.start_button = tk.Button(root, text="Start Game", command=self.start_game, bg='green', fg='white', font=('Helvetica', 14))
        self.start_button.pack(pady=10)

        self.guess_label = tk.Label(root, text="", bg='lightblue', fg='black', font=('Helvetica', 14))
        self.guess_label.pack(pady=10)

        self.guess_entry = tk.Entry(root, font=('Helvetica', 14))
        self.guess_entry.pack(pady=5)

        self.submit_button = tk.Button(root, text="Submit Guess", command=self.submit_guess, bg='blue', fg='white', font=('Helvetica', 14), state=tk.DISABLED)
        self.submit_button.pack(pady=10)

        self.feedback_label = tk.Label(root, text="", bg='lightblue', fg='black', font=('Helvetica', 14))
        self.feedback_label.pack(pady=10)

        self.score_label = tk.Label(root, text="", bg='lightblue', fg='black', font=('Helvetica', 14))
        self.score_label.pack(pady=10)

        self.reset_button = tk.Button(root, text="Reset Game", command=self.reset_game, bg='red', fg='white', font=('Helvetica', 14))
        self.reset_button.pack(pady=10)

        self.target = None
        self.guess_count = 0

    def start_game(self):
        difficulty = self.difficulty_entry.get().lower()
        if difficulty in ['easy', 'medium', 'hard']:
            self.target = self.generate_random_number(difficulty)
            self.guess_count = 0
            self.guess_label.config(text="Enter your guess:")
            self.feedback_label.config(text="")
            self.score_label.config(text="")
            self.submit_button.config(state=tk.NORMAL)
        else:
            self.feedback_label.config(text="Invalid difficulty level")

        self.guess_entry.delete(0, tk.END)

    def generate_random_number(self, difficulty):
        if difficulty == 'easy':
            return random.randint(1, 10)
        elif difficulty == 'medium':
            return random.randint(1, 100)
        elif difficulty == 'hard':
            return random.randint(1, 1000)

    def submit_guess(self):
        guess = self.guess_entry.get()
        if guess.isdigit():
            guess = int(guess)
            self.guess_count += 1
            self.provide_feedback(guess)
            self.guess_entry.delete(0, tk.END)
        else:
            self.feedback_label.config(text="Please enter a valid number.")

    def provide_feedback(self, guess):
        if guess < self.target:
            self.feedback_label.config(text="Too low!")
        elif guess > self.target:
            self.feedback_label.config(text="Too high!")
        else:
            self.feedback_label.config(text="Correct!")
            self.display_score()
            self.submit_button.config(state=tk.DISABLED)

    def display_score(self):
        score = max(100 - self.guess_count, 0)
        self.score_label.config(text=f"Congratulations! You guessed the number in {self.guess_count} tries.\nYour score: {score}")

    def reset_game(self):
        self.difficulty_entry.delete(0, tk.END)
        self.guess_entry.delete(0, tk.END)
        self.target = None
        self.guess_count = 0
        self.guess_label.config(text="")
        self.feedback_label.config(text="")
        self.score_label.config(text="")
        self.submit_button.config(state=tk.DISABLED)

def main():
    root = tk.Tk()
    game = GuessNumberGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
