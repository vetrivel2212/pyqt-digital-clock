import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatabase

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(800, 500, 500, 100)
        self.setStyleSheet("background-color: black;")

        hbox = QHBoxLayout()
        hbox.addWidget(self.time_label)
        self.setLayout(hbox)

        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("color: green;")

        # Load custom font
        font_path = r"D:\3_digitalclock\DS-DIGIT.TTF"  # <-- Change this path if needed
        font_id = QFontDatabase.addApplicationFont(font_path)
        if font_id != -1:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            my_font = QFont(font_family)
            my_font.setPointSize(60)
            self.time_label.setFont(my_font)
        else:
            print("⚠️ Failed to load custom font. Using default.")
            default_font = QFont("Arial", 60)
            self.time_label.setFont(default_font)

        # Set up timer
        self.timer.timeout.connect(self.updateTime)
        self.timer.start(1000)  # Update every second
        self.updateTime()       # Initial time display

    def updateTime(self):
        current_time = QTime.currentTime().toString("hh:mm:ss A")  # 12-hour format with AM/PM
        self.time_label.setText(current_time)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())
