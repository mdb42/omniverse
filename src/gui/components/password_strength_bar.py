from PyQt6.QtWidgets import QProgressBar
from PyQt6.QtGui import QColor
from PyQt6.QtCore import Qt

class PasswordStrengthBar(QProgressBar):
    def __init__(self, parent=None):
        super().__init__(parent)

    def update_strength(self, password):
        strength = evaluate_password_strength(password)

        # update the progress bar value
        self.setValue(strength)

        # change color based on strength
        if strength < 50:
            color = QColor(Qt.GlobalColor.red)
        elif strength < 80:
            color = QColor(Qt.GlobalColor.yellow)
        else:
            color = QColor(Qt.GlobalColor.green)

        # set the color of the progress bar
        self.setStyleSheet(f"QProgressBar::chunk "
                           f"{{ background-color: {color.name()}; }}")
        
        def evaluate_password_strength(password):
            """
            Evaluates the strength of a password based on length and complexity.
            Returns a value between 0 (weak) and 100 (strong).
            """
            strength = 0

            if len(password) >= 8:
                strength += 25
            if len(password) >= 12:
                strength += 25
            if any(char.isdigit() for char in password):
                strength += 10
            if any(char.islower() for char in password):
                strength += 10
            if any(char.isupper() for char in password):
                strength += 10
            if not password.isalnum():
                strength += 20

            return strength
