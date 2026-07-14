
classmates = ["Aarav", "Rahul", "Shreya", "Diya", "Ayshii"]
print("Class list:", classmates)

print("Total students:", len(classmates))
print("First student:", classmates[0])
print("Last student:", classmates[-1])
print("First three:", classmates[:3])

classmates.append("Ojaswita")
print("\nAfter adding Ojaswita:", classmates)
classmates.remove("Diya")
print("After removing Diya:", classmates)
classmates.sort()
print("Sorted alphabetically:", classmates)
classmates.reverse()
print("Reversed:", classmates)

teacher = {"name": "Mr. Saha", "subject": "Python", "experience": 15}
print("\nTeacher profile:", teacher)

print("Subject:", teacher["subject"])
print("Experience:", teacher.get("experience", "Not found"))
teacher["experience"] = 6
teacher["email"] = "xcellence@school.com"
teacher.pop("experience")
print("Updated teacher profile:", teacher)


roll_numbers = [1, 2, 3, 4, 5]
names = ["Aarav", "Priya", "Rahul", "Sneha", "Meera"]
student_directory = dict(zip(roll_numbers, names))
print("\nStudent Directory:", student_directory)
print("Student at Roll 3:", student_directory[3])
