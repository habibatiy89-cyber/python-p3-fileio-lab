# lib/file_io.py

def write_file(file_name, file_content):
    """
    Creates a new text file (or overwrites if it exists) and writes content to it.
    Automatically adds the '.txt' extension.
    """
    full_file_name = f"{file_name}.txt"
    with open(full_file_name, "w") as f:
        f.write(file_content)


def append_file(file_name, append_content):
    """
    Appends content directly to an existing text file.
    Automatically adds the '.txt' extension.
    """
    full_file_name = f"{file_name}.txt"
    with open(full_file_name, "a") as f:
        f.write(append_content)  # Directly append without newline


def read_file(file_name):
    """
    Reads the content of a text file and returns it as a string.
    Automatically adds the '.txt' extension.
    """
    full_file_name = f"{file_name}.txt"
    with open(full_file_name, "r") as f:
        return f.read()
