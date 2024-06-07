# Prompt the user to enter an input value and evaluate it
val = eval(input('Enter input value:\n'))

# Print the value along with its type
print('%s is a Python %s object' % (val, type(val)))

"""
Sample run:
python objects_qa.py
Enter input value:
1
1 is a Python <class 'int'> object
python objects_qa.py
Enter input value:
1.0
1.0 is a Python <class 'float'> object
python objects_qa.py
Enter input value:
1 + 1j
(1+1j) is a Python <class 'complex'> object
python objects_qa.py
Enter input value:
[1,2]
[1, 2] is a Python <class 'list'> object
python objects_qa.py
Enter input value:
(1,2)
(1, 2) is a Python <class 'tuple'> object
"""
