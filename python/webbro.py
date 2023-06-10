import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton
from PyQt5.QtWebEngineWidgets import QWebEngineView


class WebBrowser(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Web Browser')
        self.setup_ui()
        
    def setup_ui(self):
        # Create web view
        self.web_view = QWebEngineView()
        
        # Create search bar
        self.search_bar = QLineEdit()
        self.search_bar.returnPressed.connect(self.load_url)
        
        # Create navigation buttons
        self.back_button = QPushButton('Back')
        self.back_button.clicked.connect(self.web_view.back)
        
        self.forward_button = QPushButton('Forward')
        self.forward_button.clicked.connect(self.web_view.forward)
        
        # Create layout
        layout = QVBoxLayout()
        
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.back_button)
        button_layout.addWidget(self.forward_button)
        
        layout.addWidget(self.search_bar)
        layout.addLayout(button_layout)
        layout.addWidget(self.web_view)
        
        self.setLayout(layout)
        
    def load_url(self):
        url = self.search_bar.text()
        if not url.startswith('http://') and not url.startswith('https://'):
            url = 'http://' + url
        self.web_view.load(QUrl(url))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    browser = WebBrowser()
    browser.show()
    
    sys.exit(app.exec_())
