import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QTabWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView


class WebBrowser(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Web Browser')
        self.web_view = None  # Initialize web_view as None
        self.setup_ui()
        
    def setup_ui(self):
        # Create tab widget
        self.tab_widget = QTabWidget()
        self.tab_widget.setTabsClosable(True)
        self.tab_widget.tabCloseRequested.connect(self.close_tab)
        self.tab_widget.tabBarDoubleClicked.connect(self.add_tab)
        
        # Create search bar
        self.search_bar = QLineEdit()
        self.search_bar.returnPressed.connect(self.load_url)
        
        # Create navigation buttons
        self.back_button = QPushButton('Back')
        
        self.forward_button = QPushButton('Forward')
        
        # Create layout
        layout = QVBoxLayout()
        
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.back_button)
        button_layout.addWidget(self.forward_button)
        
        layout.addWidget(self.search_bar)
        layout.addLayout(button_layout)
        layout.addWidget(self.tab_widget)
        
        self.setLayout(layout)
        
        # Connect button signals after creating the layout
        self.back_button.clicked.connect(self.go_back)
        self.forward_button.clicked.connect(self.go_forward)
        
        # Create initial tab
        self.add_tab()
        
    def add_tab(self):
        # Create web view
        self.web_view = QWebEngineView()
        self.web_view.loadFinished.connect(self.update_tab_title)
        
        # Add web view to tab widget
        self.tab_widget.addTab(self.web_view, 'New Tab')
        self.tab_widget.setCurrentWidget(self.web_view)
        
        # Connect back button signal after creating web view
        self.back_button.clicked.connect(self.go_back)
        
    def close_tab(self, index):
        # Remove tab from tab widget
        self.tab_widget.removeTab(index)
        
    def load_url(self):
        url = self.search_bar.text()
        if not url.startswith('http://') and not url.startswith('https://'):
            url = 'https://' + url
        self.web_view.load(QUrl(url))
        
    def update_tab_title(self):
        # Update tab title with page title
        title = self.web_view.page().title()
        index = self.tab_widget.currentIndex()
        self.tab_widget.setTabText(index, title)
        
    def go_back(self):
        if self.web_view:
            self.web_view.back()
            
    def go_forward(self):
        if self.web_view:
            self.web_view.forward()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    browser = WebBrowser()
    browser.show()
    
    sys.exit(app.exec_())