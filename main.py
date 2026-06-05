from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit
import sys


### The Main WIndow class ###
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bird Journal 🐦")
        self.setGeometry(0,0, 600, 400)
        
        # Apply the Always on Top flag
        self.setWindowFlags(self.windowFlags() | Qt.WindowType.WindowStaysOnTopHint)
        self.show()
        self.init_ui()

    def init_ui(self):
        container = QWidget() # create a container, which holds all the other widgets.
        layout = QVBoxLayout() # q Vertical Box Layout
        container.setLayout(layout)
        self.setCentralWidget(container) # set the container as the centreral widget

        ### Ui Things ###
        add_bird_btn = QPushButton("+ Add Bird")
        add_bird_btn.clicked.connect(self.add_bird)
        add_bird_btn.setMinimumHeight(35)
        add_bird_btn.setMinimumWidth(100)
        layout.addWidget(add_bird_btn, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

    def add_bird(self):
        pass


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
