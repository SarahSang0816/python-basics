# Numeric constants
print(123)
print(98.6)

# String constants use single quote ('') or double quotes ("")
print('Hello World')
print("I love coding")

# Numeric expressions
# Parentheses --> Power --> Multiplication --> Addition --> Left to Right
x = 1 + 2 ** 3 / 4 * 5
print(x)
type(x)

# String operations
s = 'hello' + ' ' + 'welcome'
print(s)
type(s)

# Float and integer type conversion
res = print(float(99) + 100)
type(res)

# Integer division produces a floating point result in python 3
print(10 / 2)         # result is 5.0
print(9 / 2)          # result is 4.5
print(99 / 100)       # result is 0.99
print(10.0 / 2.0)

# convert string (string with numeric letters) to integer or float
sva1 = '123'
print(int(sva1) + 1)  # result is 124

# Pause and read data from the user using the input() function
# The input() function returns a string
name = input('Who are you')
print('Welcome ', name)
