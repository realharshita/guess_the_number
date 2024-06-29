import tkinter as tk
import random

class GuessNumberGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Guess the Number Game")
        self.root.configure(bg='lightblue')  # Background color

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

        self.submit_button = tk.Button(root, text="Submit Guess", command=self.submit_guess, bg='blue', fg='white', font=('Helvetica', 14))
        self.submit_button.pack(pady=10)

        self.feedback_label = tk.Label(root, text="", bg='lightblue', fg='black', font=('Helvetica', 14))
        self.feedback_label.pack(pady=10)

        self.score_label = tk.Label(root, text="", bg='lightblue', fg='black', font=('Helvetica', 14))
        self.score_label.pack(pady=10)

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
