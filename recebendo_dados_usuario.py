"""
Receiving user

input() -> Every data received with input has the type String
"""
# Input of data

print("What is your name? ")
name = input()

# Example in old way
# print("You are welcome %s" % name)

# Example of modern print
# print('You are welcome {0}'.format(name))

# Example of actual print
print(f'You are welcome {name}')

print("How old are you? ")
age = input()

# Process

# Output of data
# Example in old way
# print("%s has %s years" % (name, age))

# Example of modern print
# print('{0} has {1} years'.format(name, age))

# Example of actual print
print(f'{name} has {age}')

""""
# int(age) => cast

Cast is the conversion of a type of data to another.

"""
print(f'{name} was born in {2023 - int(age)}')

'''
Simple way, less code:
name = int(input('What is your name? '))
age = int(input('What is your age? '))
print(f'{name} was born in {2023 - age}')
'''
