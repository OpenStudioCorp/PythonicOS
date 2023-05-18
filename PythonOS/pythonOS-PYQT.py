import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QAction, QDesktopWidget, QLabel, QWidget, QGridLayout, QFileDialog
from PyQt5.QtGui import QIcon, QPixmap, QCursor
from PyQt5.QtCore import Qt, QUrl, QStandardPaths
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag, QCursor
from PyQt5.QtWidgets import QApplication, QLabel
import subprocess
class Desktop(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Desktop")
        self.setGeometry(100, 100, 600, 50)
        self.setStyleSheet("background-color: #f0f0f0;")
        self.icons_layout = QGridLayout()
        self.icons_layout.setSpacing(20)
        self.icons_widget = QWidget()
        self.icons_widget.setLayout(self.icons_layout)
        self.setCentralWidget(self.icons_widget)
        self.load_icons()

    def load_icons(self):
        folder_path = "PythonOS/home"  # Specify the path to the folder containing the files, change from PythonOS/home to Home when running within the idle or for building
        files = os.listdir(folder_path)
        icon_size = (1 * 80, 1 * 80)  # 5 inches in width and height (assuming 96 DPI)
        max_columns = 20  # Maximum number of columns, change this if you want more items on one row!
        row = 0
        col = 0
        for file_name in files:
            file_path = os.path.join(folder_path, file_name)
            icon_label = QLabel(file_name)
            icon_label.setFixedSize(*icon_size)
            icon_label.setStyleSheet(
                "QLabel { background-color: #007bff; color: white; font-size: 12pt; padding: 8px; border-radius: 4px; }"
            )
            icon_label.setToolTip(file_path)
            self.icons_layout.addWidget(icon_label, row, col)

            col += 1
            if col >= max_columns:
                col = 0
                row += 1

        # Set column stretch to allow wrapping when the window size is too small
        self.icons_layout.setColumnStretch(max_columns, 1)

    def open_file(self, file_path):
        print()
        subprocess.Popen(['python','addons/panno.py'])  # Open the file using the default associated program

    def contextMenuEvent(self, event):
        context_menu = QMenu(self)
        create_file_action = QAction("Create File", self)
        create_file_action.triggered.connect(self.create_file)
        context_menu.addAction(create_file_action)
        context_menu.exec_(QCursor.pos())

    def create_file(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Create File", "", "Text Files (*.txt)")
        if file_name:
            open(file_name, "w").close()
            self.load_icons()

def main():
    app = QApplication(sys.argv)
    desktop = Desktop()
    desktop.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
