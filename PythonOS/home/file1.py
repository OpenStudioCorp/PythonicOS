import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QAction
from file import home_dir
home_directory = home_dir
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

def create_file(home_directory):
    # create home directory if it doesn't exist
    if not os.path.exists(home_directory):
        os.mkdir(home_directory)

    # create filename
    filename = 'file{}.py'.format(len(os.listdir(home_directory)))

    # create file path
    file_path = os.path.join(home_directory, filename)

    # write to file
    if not os.path.isfile(file_path):
        with open(file_path, 'w') as file:
            file.write('This is the content of {}\n'.format(filename))
            print("File created: {}".format(filename))
    else:
        print("File already exists: {}".format(filename))

    # reload files



    def initUI(self):
        self.setWindowTitle("Right-click Context Menu Example")
        self.setGeometry(300, 300, 800, 600)

    def contextMenuEvent(self, event):
        context_menu = QMenu(self)

        new_action = QAction("New", self)
        new_action.triggered.connect(self.new_action_triggered)
        context_menu.addAction(new_action)

        edit_action = QAction("Edit", self)
        edit_action.triggered.connect(self.edit_action_triggered)
        context_menu.addAction(edit_action)

        quit_action = QAction("Quit", self)
        quit_action.triggered.connect(self.quit_action_triggered)
        context_menu.addAction(quit_action)

        context_menu.exec_(event.globalPos())

    def new_action_triggered(self):
        print("New action triggered")

    def edit_action_triggered(self):
        print("Edit action triggered")

    def quit_action_triggered(self):
        QApplication.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
