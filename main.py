import sys
import random
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from hangman_game_logic import GameLogic
from hangman_game_ui import UI

class Main:
    def __init__(self):
        self.game_logic = GameLogic()
        self.ui = UI(self.game_logic)

    def run(self):
        app = QApplication(sys.argv)
        self.ui.show()
        sys.exit(app.exec_())
    
if __name__ == '__main__':
    # Create the QApplication instance
    app = QApplication(sys.argv)

    # Create the GameLogic instance
    game_logic = GameLogic('words.txt')


    # Create the UI instance and show it
    ui = UI(game_logic)
    ui.show()

    # Run the event loop
    sys.exit(app.exec_())
