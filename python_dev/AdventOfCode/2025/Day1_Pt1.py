import os

print(os.getcwd())

with open("/input.txt", "r") as f:
    contents = f.read()
    print(contents)