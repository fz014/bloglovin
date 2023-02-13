# 1: String 
print("Hello world")

print('''I wandered lonely as a cloud
That floats on high o'er vales and hills,
When all at once I saw a crowd,
A host, of golden daffodils;
Beside the lake, beneath the trees,
Fluttering and dancing in the breeze.''')

#2: Module 
# We will import the external module 
#install the external module [playsound]
from playsound import playsound
playsound('C:\\Users\\PC\\Desktop\\semester 7\\web design\\codes of python\\play.mp3')

#3: Lists
#Lists with integer 
a=[1,2,3]
print(a)
#output = [1,2,3]

# empty list
my_list = []

# list with mixed data types
my_list = [1, "Hello", 3.4]

languages = ["Python", "Swift", "C++"]

# access item at index 0
print(languages[0])

#4: Tuple
# Example 1: A tuple with integer elements
integer_tuple = (1, 2, 3, 4, 5)
print(integer_tuple)
# Output: (1, 2, 3, 4, 5)

# Example 2: A tuple with mixed elements
mixed_tuple = (1, "hello", 3.14, True)
print(mixed_tuple)
# Output: (1, "hello", 3.14, True)

# Example 3: A tuple with nested elements
nested_tuple = (1, (2, 3), [4, 5])
print(nested_tuple)
# Output: (1, (2, 3), [4, 5])

# Example 4: A single-element tuple
single_tuple = (1,)
print(single_tuple)
# Output: (1,)

#5: Dictionary 
# Example 1: A dictionary with integer keys and values
integer_dic = {1: 10, 2: 20, 3: 30}
print(integer_dic)
# Output: {1: 10, 2: 20, 3: 30}

# Example 2: A dictionary with string keys and values
string_dic = {"one": 1, "two": 2, "three": 3}
print(string_dic)
# Output: {'one': 1, 'two': 2, 'three': 3}

# Example 3: A dictionary with mixed keys and values
mixed_dic = {1: "one", "two": 2, 3: [1, 2, 3]}
print(mixed_dic)
# Output: {1: 'one', 'two': 2, 3: [1, 2, 3]}

#6: If condition
num = 5
if num > 0:
    print("positive")
else:
    print("negative")
# Output: positive

#7: While loop 

# Code to be executed as long as the condition is True
#Example 1:
count = 1
while count <= 5:
    print(count)
    count += 1
# Output:
# 1
# 2
# 3
# 4
# 5

#8: for loop 
#Example:
fruits = ['peach', 'guava', 'grapes']
for fruit in fruits:
    print(fruit)
# Output:
# peach
# guava
# grapes

#9: Range in python 
# Generate a range of numbers from 0 to 9
for num in range(10):
    print(num)
# Output:
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

#10: Break statement in python 

names = ['fiza', 'maham', 'salma', 'mita']
for name in names:
    if name == 'salma':
        print("Found maham, breaking loop")
        break
    print(name)
# Output:
# fiza
# maham
# Found salma, breaking loop      