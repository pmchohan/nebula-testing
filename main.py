import os

dir_path = os.path.dirname(__file__)
file_path = os.path.join(dir_path, 'data', 'example.txt')

with open(file_path, 'w') as file:
    file.write("Hello, World!")
    file.write("\nThis is a test file.")
    file.write("\nIt contains multiple lines of text.")
    file.write("\nGoodbye!")
