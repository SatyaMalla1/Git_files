print("python")
print("")

name = "Satya1"
age = 29

print(name)
print(age)

print("")
for i in range(5):
    print(i)

print("")
if age > 18:
    print("Adult")

print("")
def greet(name):
    print("Hello", name)

greet("Satya2")

fruits = ["apple", "banana", "mango"]
person = {"name": "Satya", "city": "White Plains"}

print("")
print(fruits)
print(fruits[1])

print("")
print(person)
print(person["city"])

print("")
for i in range(len(fruits)):
    print(i, fruits[i])

print("")
for key, value in person.items():
    print(key, ":", value)

print("")
people = [
    {"name": "Satya", "city": "White Plains"},
    {"name": "John", "city": "NYC"}
]

for p in people:
    print(p["name"], "-", p["city"])

