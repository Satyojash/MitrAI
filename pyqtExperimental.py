# import sys
# from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Hello PyQt")
#         label = QLabel("Hello, Mitr AI!", self)
#         self.setCentralWidget(label)

# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
# sys.exit(app.exec_())
#-------------------------------------------------------------------------

import sys
from PyQt5.QtCore import Qt, QPropertyAnimation, QRect
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QEasingCurve

class FloatingWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set window flags to make it borderless, transparent, and always on top
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)

        # Make the window transparent
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Set up the appearance of the floating window (example: a label with text)
        self.initUI()

    def initUI(self):
        # Set up label or any UI you want for your assistant
        label = QLabel('Hey, I am Your MiTR!', self)
        label.setFont(QFont('Arial', 25))
        label.setStyleSheet('color: white; background-color: rgba(0, 0, 0, 150); padding: 20px; border-radius: 20px;')
        
        # Resize the window
        self.resize(300, 150)

        # Place the window in the middle bottom of the screen (off-screen initially for animation)
        screen_geometry = QApplication.desktop().screenGeometry()
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()

        self.final_x = (screen_width - self.width()) // 2
        self.final_y = screen_height - self.height() - 50  # Adjust to bottom

        # Start the window off-screen (below the screen)
        self.move(self.final_x, screen_height)

        # Run the in-animation
        self.run_animation()

    def run_animation(self):
        # Create the animation object
        self.animation = QPropertyAnimation(self, b"geometry")
        self.animation.setDuration(800)  # Duration of the animation in ms
        self.animation.setStartValue(QRect(self.final_x, QApplication.desktop().screenGeometry().height(), self.width(), self.height()))  # Start below the screen
        self.animation.setEndValue(QRect(self.final_x, self.final_y, self.width(), self.height()))  # End at the middle-bottom
        self.animation.setEasingCurve(QEasingCurve.OutBounce)  # Smooth sliding with bounce effect

        # Start the animation
        self.animation.start()

    # Optional: If you want the window to be draggable
    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = event.globalPos() - self.oldPos
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Create the floating window
    floating_window = FloatingWindow()
    floating_window.show()

    sys.exit(app.exec_())


