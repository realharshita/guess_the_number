import tkinter as tk
from tkinter import messagebox
import random
import pygame

class GuessNumberGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Guess the Number Game")
        self.root.configure(bg='lightblue')

        pygame.mixer.init()
        self.correct_sound = pygame.mixer.Sound("correct.wav")
        self.incorrect_sound = pygame.mixer.Sound("incorrect.wav")

        self.label = tk.Label(root, text="Welcome to the Guess the Number Game!", bg='lightblue', fg='black', font=('Helvetica', 16), borderwidth=2, relief="groove")
        self.label.pack(pady=10)

        self.difficulty_label = tk.Label(root, text="Select difficulty level: easy, medium, hard", bg='lightblue', fg='black', font=('Helvetica', 14), borderwidth=2, relief="groove")
        self.difficulty_label.pack()

        self.difficulty_entry = tk.Entry(root, font=('Helvetica', 14), borderwidth=2, relief="groove")
        self.difficulty_entry.pack(pady=5)

        self.start_button = tk.Button(root, text="Start Game", command=self.start_game, bg='green', fg='white', font=('Helvetica', 14), borderwidth=2, relief="raised")
        self.start_button.pack(pady=10)

        self.guess_label = tk.Label(root, text="", bg='lightblue', fg='black', font=('Helvetica', 14), borderwidth=2, relief="groove")
        self.guess_label.pack(pady=10)

        self.guess_entry = tk.Entry(root, font=('Helvetica', 14), borderwidth=2, relief="groove")
        self.guess_entry.pack(pady=5)

        self.submit_button = tk.Button(root, text="Submit Guess", command=self.submit_guess, bg='blue', fg='white', font=('Helvetica', 14), state=tk.DISABLED, borderwidth=2, relief="raised")
        self.submit_button.pack(pady=10)

        self.feedback_label = tk.Label(root, text="", bg='lightblue', fg='black', font=('Helvetica', 14), borderwidth=2, relief="groove")
        self.feedback_label.pack(pady=10)

        self.score_label = tk.Label(root, text="", bg='lightblue', fg='black', font=('Helvetica', 14), borderwidth=2, relief="groove")
        self.score_label.pack(pady=10)

        self.high_score_label = tk.Label(root, text="", bg='lightblue', fg='black', font=('Helvetica', 14), borderwidth=2, relief="groove")
        self.high_score_label.pack(pady=10)

        self.timer_label = tk.Label(root, text="", bg='lightblue', fg='black', font=('Helvetica', 14), borderwidth=2, relief="groove")
        self.timer_label.pack(pady=10)

        self.reset_button = tk.Button(root, text="Reset Game", command=self.reset_game, bg='red', fg='white', font=('Helvetica', 14), borderwidth=2, relief="raised")
        self.reset_button.pack(pady=10)

        self.target = None
        self.guess_count = 0
        self.high_score = self.load_high_score()

        self.timer_seconds = 60
        self.timer_running = False

    def start_game(self):
        if not self.timer_running:
            difficulty = self.difficulty_entry.get().lower()
            if difficulty in ['easy', 'medium', 'hard']:
                self.target = self.generate_random_number(difficulty)
                self.guess_count = 0
                self.guess_label.config(text="Enter your guess:")
                self.feedback_label.config(text="")
                self.score_label.config(text="")
                self.submit_button.config(state=tk.NORMAL)
                self.start_timer()
            else:
                self.feedback_label.config(text="Invalid difficulty level", bg='red')
                self.root.after(2000, lambda: self.feedback_label.config(bg='lightblue'))

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
            self.feedback_label.config(text="Please enter a valid number.", bg='red')
            self.root.after(2000, lambda: self.feedback_label.config(bg='lightblue'))

    def provide_feedback(self, guess):
        if guess < self.target:
            self.feedback_label.config(text="Too low!", bg='orange')
            self.incorrect_sound.play()
            self.root.after(2000, lambda: self.feedback_label.config(bg='lightblue'))
        elif guess > self.target:
            self.feedback_label.config(text="Too high!", bg='orange')
            self.incorrect_sound.play()
            self.root.after(2000, lambda: self.feedback_label.config(bg='lightblue'))
        else:
            self.feedback_label.config(text="Correct!", bg='green')
            self.correct_sound.play()
            self.display_score()
            self.submit_button.config(state=tk.DISABLED)
            if self.guess_count < self.high_score:
                self.save_high_score(self.guess_count)
                self.high_score_label.config(text=f"New High Score: {self.guess_count}")
            else:
                self.high_score_label.config(text=f"High Score: {self.high_score}")

    def display_score(self):
        score = max(100 - self.guess_count, 0)
        self.score_label.config(text=f"Congratulations! You guessed the number in {self.guess_count} tries.\nYour score: {score}")

    def reset_game(self):
        self.difficulty_entry.delete(0, tk.END)
        self.guess_entry.delete(0, tk.END)
        self.target = None
        self.guess_count = 0
        self.guess_label.config(text="")
        self.feedback_label.config(text="", bg='lightblue')
        self.score_label.config(text="")
        self.submit_button.config(state=tk.DISABLED)
        self.stop_timer()
        self.timer_seconds = 60

    def load_high_score(self):
        try:
            with open('high_score.txt', 'r') as file:
                return int(file.read().strip())
        except FileNotFoundError:
            return float('inf')
        except ValueError:
            return float('inf')

    def save_high_score(self, score):
        with open('high_score.txt', 'w') as file:
            file.write(str(score))

    def start_timer(self):
        self.timer_running = True
        self.update_timer()

    def stop_timer(self):
        self.timer_running = False

    def update_timer(self):
        if self.timer_seconds > 0 and self.timer_running:
            self.timer_label.config(text=f"Time left: {self.timer_seconds} seconds")
            self.timer_seconds -= 1
            self.root.after(1000, self.update_timer)
        else:
            self.timer_label.config(text="Time's up!")
            self.stop_game()

    def stop_game(self):
        self.submit_button.config(state=tk.DISABLED)
        self.timer_running = False

def main():
    root = tk.Tk()
    game = GuessNumberGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
