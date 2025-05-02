import sys
from tkinter import messagebox
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QTextEdit,
    QPushButton,
    QCalendarWidget,
)
from PyQt5.QtGui import QFont, QPalette, QColor
from PyQt5.QtCore import Qt, QLocale
class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("EthniCity")
        self.resize(800, 600)  # Adjust window size as needed
        self.set_ui()

    def set_ui(self):
        good_light_blue = QColor(217,224,226)
        good_light_white = QColor(244,243,243)
        good_dark_blue = QColor(143,146,148)
        good_dark_black = QColor(31,34,43)
        # Create main layout (vertical with spacing)
        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(15)  # Add some spacing between elements

        # Set a beautiful background color (lavender)
        palette = QPalette()
        palette.setColor(QPalette.Window, good_light_blue)  # Light lavender
        self.setPalette(palette)

        # Header section
        header_label = QLabel("Cultural and Awareness Hub")
        header_label.setFont(QFont("Arial", 20, weight=QFont.Bold))
        header_label.setStyleSheet("color: " + good_dark_black.name() + ";") # White text for header
        main_layout.addWidget(header_label)

        # Input sections (General and Culinary)
        input_sections_layout = QHBoxLayout()
        input_sections_layout.setSpacing(10)  # Spacing between input sections
        main_layout.addLayout(input_sections_layout)

        general_section = self.create_input_section("General")
        culinary_section = self.create_input_section("Culinary")
        input_sections_layout.addWidget(general_section)
        input_sections_layout.addWidget(culinary_section)

        # Cultural data display section
        cultural_data_label = QLabel("Cultural contents:")
        cultural_data_label.setFont(QFont("Arial", 16))
        main_layout.addWidget(cultural_data_label)

        cultural_data_display = QTextEdit(readOnly=True)
        cultural_data_display.setFont(QFont("Arial", 12))
        cultural_data_display.setStyleSheet("color: " + good_light_white.name() + ";") # Light gray background
        main_layout.addWidget(cultural_data_display)

        # Calendar and alerts section (mockup, not functional)
        calendar_alerts_layout = QHBoxLayout()
        main_layout.addLayout(calendar_alerts_layout)

        calendar_widget = QCalendarWidget()
        calendar_widget.setGridVisible(True)

        calendar_widget.setStyleSheet("QCalendarWidget { background-color: " + good_light_white.name() + "; }")
        # Set locale to English
        calendar_widget.setLocale(QLocale(QLocale.English))
        calendar_alerts_layout.addWidget(calendar_widget)




        alerts_button = QPushButton("Real-Time Cultural Alerts")
        alerts_button.clicked.connect(self.mock_alert)  # Connect to a mock alert function
        alerts_button.setStyleSheet("background-color:"+ good_dark_blue.name()+"; color: white ; padding: 5px 10px; border-radius: 5px;")  # Purple button with white text
        calendar_alerts_layout.addWidget(alerts_button)

        self.setLayout(main_layout)


    def create_input_section(self, title):
        section_widget = QWidget()
        section_layout = QVBoxLayout(section_widget)

        section_label = QLabel(title)
        section_label.setFont(QFont("Arial", 14, weight=QFont.Bold))
        section_layout.addWidget(section_label)

        # Add input fields (cultural practices, holidays, etc.) based on your requirements
        # (e.g., QLineEdit, QComboBox, QTextEdit)
        cultural_practices_input = QLineEdit()
        cultural_practices_input.setPlaceholderText("Enter cultural practices...")
        section_layout.addWidget(cultural_practices_input)

        # ... (add more input fields as needed)

        return section_widget

    def mock_alert(self):
        # Display a mock message box for demonstration purposes
        message_box = messagebox()
        message_box.setWindowTitle("Real-Time Cultural Alert")
        message_box.setText("This is a mock alert for demonstration.")
        message_box.setIcon(messagebox.Information)
        message_box.setStandardButtons(messagebox.Ok)
        message_box.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)  # Remove the extra indentation here
    window = MainWindow()
    window.show()
    app.exec_()
