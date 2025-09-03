#with open("file handling/input.txt", 'w') as file:
#    file.write(
#        "Hello, Welcome to my program!, here, we are learning about file handling in Python."
#        "\nPython is a versatile language. It supports multiple programming paradigms."
#        "\nFile handling is an essential part of any programming language."
#        "\nIn this program, we will explore how to read and write files in Python."
#    )
#print("File created and text written successfully.")

with open("file handling/input.txt", 'r') as file:
    info = file.read()
    word_count = 0
    for line in info.split('\n'):
        for word in line.split():
            word_count += 1
    
    processed_text = info.upper()
    with open("file handling/output.txt", 'w') as file:
        file.write(processed_text)
    print(f"Total number of words: {word_count}, and New file created successfully.")
    

