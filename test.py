import sys
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
    QMessageBox
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
        good_dark_blue = QColor(143,146,148)
        good_dark_black = QColor(31,34,43)

        # Create main layout (vertical with spacing)
        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(15)  # Add some spacing between elements

        # Set a beautiful background color
        palette = QPalette()
        palette.setColor(QPalette.Window, good_light_blue)
        self.setPalette(palette)

        # Header section
        header_label = QLabel("Cultural and Culinary Awareness Hub")
        header_label.setFont(QFont("Arial", 20, weight=QFont.Bold))
        header_label.setStyleSheet("color: " + good_dark_black.name() + ";")
        main_layout.addWidget(header_label)

        # Input sections (General and Culinary)
        input_sections_layout = QHBoxLayout()
        input_sections_layout.setSpacing(10)
        main_layout.addLayout(input_sections_layout)

        general_section = self.create_input_section("Holiday Descriptions and Customs")
        culinary_section = self.create_input_section("Culinary Customs")
        input_sections_layout.addWidget(general_section)
        input_sections_layout.addWidget(culinary_section)

        # Cultural data display section
        cultural_data_label = QLabel("Cultural contents:")
        cultural_data_label.setFont(QFont("Arial", 16))
        main_layout.addWidget(cultural_data_label)

        cultural_data_display = QTextEdit(readOnly=True)
        cultural_data_display.setFont(QFont("Arial", 12))
        cultural_data_display.setStyleSheet("color: white;")
        main_layout.addWidget(cultural_data_display)

        # Calendar and alerts section
        calendar_alerts_layout = QVBoxLayout()  # Changed to QVBoxLayout
        main_layout.addLayout(calendar_alerts_layout)

        calendar_widget = QCalendarWidget()
        calendar_widget.setGridVisible(True)
        calendar_widget.setStyleSheet("QCalendarWidget { background-color: white; }")
        calendar_widget.setLocale(QLocale(QLocale.English))
        calendar_alerts_layout.addWidget(calendar_widget)

        alerts_button = QPushButton("Real-Time Alerts")
        alerts_button.setFont(QFont("Arial", 16, weight=QFont.Bold))
        alerts_button.clicked.connect(self.mock_alert)
        alerts_button.setStyleSheet("background-color:"+ good_light_blue.name()+"; color: "+ good_dark_black.name()+"; padding: 5px 10px; border-radius: 5px;")
        calendar_alerts_layout.addWidget(alerts_button)


        self.alerts_display = QTextEdit(readOnly=True)
        self.alerts_display.setFont(QFont("Arial", 12))
        self.alerts_display.setStyleSheet("color: " + good_dark_black.name() + "; background-color: white;")
        calendar_alerts_layout.addWidget(self.alerts_display)

        self.setLayout(main_layout)

    def create_input_section(self, title):
        section_widget = QWidget()
        section_layout = QVBoxLayout(section_widget)

        section_label = QLabel(title)
        section_label.setFont(QFont("Arial", 14, weight=QFont.Bold))
        section_layout.addWidget(section_label)

        cultural_practices_input = QLineEdit()
        cultural_practices_input.setPlaceholderText("Enter cultural practices...")
        section_layout.addWidget(cultural_practices_input)

        return section_widget

    def mock_alert(self):
        # Display a mock message box for demonstration purposes
        self.alerts_display.append("Real-Time Cultural Alert: This is a mock alert for demonstration.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
