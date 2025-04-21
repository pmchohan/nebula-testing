# Hello World

## main.py Documentation

- **Purpose**: The script creates a directory named `data` in the same location as the script itself, and writes a file named `example.txt` within that directory.
- **Functionality**:
  - Creates a directory if it doesn't exist.
  - Writes multiple lines of text to `example.txt`.

### Code

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
