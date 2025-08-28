#dictionary of students
students={
    "Rahul": 85,
    "Aman": 90,
    "Tanuj": 78,
    "Rohit": 92,
    "Mota": 88
}
name = input("enter student's name: ")
if name in students:
    print(f"{name}'s marks: ", students[name])
else:
      print(f"student's data is not in the dictionary")
