filename = "sample.txt"
try:
    with open("sample.txt") as file:
        print("Reading the file")
        line_number = 1
        for line in file:
            print(f"{line_number} : {line.strip()}")
            line_number += 1
except FileNotFoundError:
    print(f"Error:The file {filename} was not found.")

