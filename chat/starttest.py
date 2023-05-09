import subprocess
import os
import sys
def main():
    result = subprocess.run([sys.executable, 'loginscreen.py'], capture_output=True, text=True)
    print(result.stdout)