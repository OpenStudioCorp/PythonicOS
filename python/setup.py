import os

DIRS = [
    'home',
    'bin',
    'scripts',
    'addons',
    'documents',
    'home/user',
    'home/user/documents',
    'home/user/documents/projects',
    'system',
    'system/scripts',
    'system/logs'
    'mount'
]
# Why are there different files that create directories?
def main():
    for i in DIRS:
        if not os.path.exists(i):
            os.makedirs(i)
