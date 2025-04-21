# Hello World!

## Documentation for `main.py`

- **Purpose**: This script creates a directory named `data` and writes a text file named `example.txt` within it.
- **Functionality**:
  - Creates a directory if it doesn't exist.
  - Writes multiple lines of text to a file.

### Code Overview
```python
import os

dir_path = os.path.join(os.path.dirname(__file__), 'data')
file_path = os.path.join(dir_path, 'example.txt')

os.makedirs(dir_path, exist_ok=True)

with open(file_path, 'w') as file:
    file.write("Hello, World!")
    file.write("\nThis is a test file.")
    file.write("\nIt contains multiple lines of text.")
    file.write("\nGoodbye!")
```
