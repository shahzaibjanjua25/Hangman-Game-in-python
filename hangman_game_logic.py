import sys
import random
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
class GameLogic:
    def __init__(self):
        self.words = ['python', 'java', 'javascript', 'ruby', 'php', 'csharp', 'swift', 'kotlin']
        self.current_word = ''
        self.guessed_letters = []
        self.num_guesses = 0
        self.max_guesses = 6

    def reset_game(self):
        self.current_word = random.choice(self.words)
        self.guessed_letters = []
        self.num_guesses = 0
    def get_hint(self):
        # Get all the letters in the current word that have not been guessed yet
        unguessed_letters = [letter for letter in self.current_word if letter not in self.guessed_letters]

        # If all letters have been guessed, return None
        if not unguessed_letters:
            return None

        # Return a random unguessed letter
        return random.choice(unguessed_letters)

    def guess_letter(self, letter):
        if letter not in self.guessed_letters:
            self.guessed_letters.append(letter)
            if letter not in self.current_word:
                self.num_guesses += 1

    def get_current_word(self):
        return self.current_word

    def get_guessed_letters(self):
        return self.guessed_letters

    def get_num_guesses(self):
        return self.num_guesses

    def get_max_guesses(self):
        return self.max_guesses

    def is_game_over(self):
        return self.num_guesses >= self.max_guesses or set(self.guessed_letters) == set(self.current_word)

    def is_won(self):
        return set(self.guessed_letters) == set(self.current_word)

    def get_remaining_guesses(self):
        return self.max_guesses - self.num_guesses

    def get_word_display(self):
        return ''.join([c if c in self.guessed_letters else '_' for c in self.current_word])
