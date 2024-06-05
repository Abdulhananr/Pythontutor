for i in range(0,100):
	print(i)
i=0
while i<5:
	print(i)
	i=i+1
# Here are the examples of using loops with lists, dictionaries, and tuples:

#Lists

#For Loop

numbers = [1, 2, 3, 4, 5]
for number in numbers:
	print(number * 2)

#While Loop

numbers = [1, 2, 3, 4, 5]
i = 0
while i < len(numbers):
	print(numbers[i] * 2)
	i += 1

#Dictionaries

#For Loop

person = {'name': 'John', 'age': 30, 'city': 'New York'}
for key, value in person.items():
	print(f"{key}: {value}")

#While Loop

person = {'name': 'John', 'age': 30, 'city': 'New York'}
i = 0
while i < len(person):
	key = list(person.keys())[i]
	value = person[key]
	print(f"{key}: {value}")
	i += 1

#Tuples For Loop

colors = ('red', 'green', 'blue')
for color in colors:
	print(color.upper())

# While Loop

colors = ('red', 'green', 'blue')
i = 0
while i < len(colors):
	print(colors[i].upper())
	i += 1

