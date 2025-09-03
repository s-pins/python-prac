filename = input("Enter the filename: ")
base_path = "file handling/"
try:
    with open(base_path +filename, 'r') as file:
        info = file.read()
        print("File reading successful.")
except FileNotFoundError:
    print("File not found. Please check the filename and try again.")
except Exception:
    print("An error occurred while reading the file")
