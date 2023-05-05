from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebKitWidgets import QWebView  # or use QWebEngineView for PyQt5 >= 5.12

import sys

# Retrieve the file location from the command-line arguments
file_path = sys.argv[1]

app = QApplication(sys.argv)

web_view = QWebView()  # or use QWebEngineView for PyQt5 >= 5.12

# Load the local file
web_view.load(QUrl.fromLocalFile(file_path))

# Show the web view
web_view.show()

sys.exit(app.exec_())
