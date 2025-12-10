students = ["Аня", "Боря", "Вова", "Галя"]

print(students)

students.append("Дима")
print(students)

students.insert(2, "Женя")
print(students)

students.pop(2)
print(students)

print(students[1])

print(len(students))

for s in students:
    print(s)

if "Вова" in students:
    print("Вова найден")

students.sort()
print(students)

students.reverse()
print(students)
