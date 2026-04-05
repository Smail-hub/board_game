import os

os.makedirs("my_folder", exist_ok=True)

file_path = os.path.join("my_folder", "hello.txt")

with open(file_path, "w", encoding="utf8") as file:
    file.write("Hello, world!")