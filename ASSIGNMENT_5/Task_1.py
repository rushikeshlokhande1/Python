student={"Rushi":96,
           "Aniket":89,
           "Vaishnav":85,
           "Madhura":91,
           "Rahul":89}
name=input("Enter the student Name: ")
if name in student:
    print(f"{name} marks: {student[name]} ")
else:
    print(f"Student {name} not found")