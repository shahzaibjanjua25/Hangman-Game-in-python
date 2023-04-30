from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox


class UI(QWidget):
    def __init__(self, game_logic):
        super().__init__()
        
        self.game_logic = game_logic

        # Set up the UI widgets
        self.word_label = QLabel()
        self.word_label.setAlignment(Qt.AlignCenter)
        self.word_label.setStyleSheet("font-size: 24px; font-weight: bold;")

        self.guess_label = QLabel()
        self.guess_label.setAlignment(Qt.AlignCenter)
        self.guess_label.setStyleSheet("font-size: 18px;")

        self.guess_input = QLineEdit()
        self.guess_input.setAlignment(Qt.AlignCenter)
        self.guess_input.setStyleSheet("font-size: 18px;")

        self.guess_button = QPushButton('Guess')
        self.guess_button.setStyleSheet("font-size: 18px; background-color: #4CAF50; color: white; border-radius: 8px;")
        
        self.new_game_button = QPushButton('New Game')
        self.new_game_button.setStyleSheet("font-size: 18px; background-color: #008CBA; color: white; border-radius: 8px;")
        
        self.hint_button = QPushButton('Hint')
        self.hint_button.setStyleSheet("font-size: 18px; background-color: #f44336; color: white; border-radius: 8px;")
        
        # Set up the image label
        self.image_label = QLabel()
        pixmap = QPixmap("hangman0.jpg").scaled(300, 300, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.image_label.setPixmap(pixmap)

        # Set up the layout
        layout = QVBoxLayout()
        layout.addWidget(self.word_label)
        layout.addWidget(self.guess_label)
        layout.addWidget(self.image_label)
        layout.addSpacing(20)
        
        guess_layout = QHBoxLayout()
        guess_layout.addStretch()
        guess_layout.addWidget(self.guess_input)
        guess_layout.addWidget(self.guess_button)
        guess_layout.addStretch()
        
        layout.addLayout(guess_layout)
        
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.new_game_button)
        button_layout.addWidget(self.hint_button)
        
        layout.addLayout(button_layout)
        layout.addStretch()
        
        self.setLayout(layout)

        # Connect signals to slots
        self.guess_button.clicked.connect(self.handle_guess)
        self.new_game_button.clicked.connect(self.handle_new_game)
        self.hint_button.clicked.connect(self.handle_hint)
        
        

        # Update the UI
        self.update_ui()

    def update_ui(self):
        word = ''.join([c if c in self.game_logic.guessed_letters else '_' for c in self.game_logic.current_word])
        self.word_label.setText(word)
        self.guess_label.setText('Guesses: ' + str(self.game_logic.num_guesses))

    def handle_guess(self):
        guess = self.guess_input.text()
        if guess.isalpha() and len(guess) == 1:
            self.game_logic.guess_letter(guess)
            self.update_ui()
            self.guess_input.setText('')
        else:
            QMessageBox.warning(self, "Invalid Guess", "Please enter a single alphabetical character", QMessageBox.Ok)

    def handle_new_game(self):
        self.game_logic.reset_game()
        self.update_ui()
        
    def handle_hint(self):
        hint = self.game_logic.get_hint()
        QMessageBox.information(self, "Hint", hint, QMessageBox.Ok)
