file_name="output.txt"
with open("output.txt",'w') as file:
    writting=input("Enter text to write to the file: ")
    file.write(writting)
    print(f"Data successfully written to {file_name}")
with open("output.txt",'a') as file:
    append=input("Enter text to append to the file: ")
    file.write(append)
    print(f"Data successfully written to {file_name}")
with open("output.txt",'r') as file:
    read=file.read()
    print(read)
