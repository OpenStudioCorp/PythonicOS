import os
import sys
import datetime
# this file was made by h4lrdev!
# and i, charlie ported it over and added stuff to the file!, thanks h4lrdev for cloning our repo! 
DIRS = [
    'sys'
    'system',
    'system/home',
    'system/bin',
    'system/scripts',
    'system/addons',
    'system/documents',
    'system/home/user',
    'system/home/user/documents',
    'system/home/user/documents/projects',
    'system/logs'
    'system/welcome'
    'system/welcome/bin'
    'mount'
]

def start():
    for i in DIRS:
        if not os.path.exists(i):
            os.makedirs(i)
def copy_folder_contents():
    # Specify the source and destination folder paths
    source_folder = 'python'
    destination_folder = 'sys'

    # Get the list of files in the source folder
    files = os.listdir(source_folder)

    # Iterate over the files and copy them to the destination folder
    for file_name in files:
        source_file = os.path.join(source_folder, file_name)
        destination_file = os.path.join(destination_folder, file_name)
        shutil.copy(source_file, destination_file)

print("Files copied successfully!")
print("you can now run "'python main.py')
def main():
    print("welcome to the setup wizard for pythonicOS!")
    print("this installer will install PythonicOS and its files into a folder")
