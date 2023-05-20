import sys
import os

# Get the path of the script or executable file
script_path = sys.argv[0]

# Get the directory containing the script or executable file
directory = os.path.dirname(os.path.abspath(script_path))

print(directory)
