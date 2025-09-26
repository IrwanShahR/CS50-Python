students = ["Hermione", "Harry", "Ron", "Draco"]

for i in range(len(students)):
    print(i+1,students[i])


houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

dict = dict(zip(students, houses))
print(dict)


print(dict["Draco"])

#by default it will only iterate over the keys
for i in dict:
    print(i)

#use index to iterate over the values
for i in dict:
    print(dict[i])


#list of dictionary

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in students:
    print(student["patronus"], student["name"], sep=",")
