'''
pseudocode
no need to worry about zero division or input errors etc.
1. ask user for an arthimetic expression
2. print the output as a float to 1 decimal place
'''

# .split() method allows each split to be assigned an indepdent variable
x, y, z = input('Enter expression: ').split(' ')
# converted to float in each conditional originally
# pointless when floats are always needed
x = float(x)
z = float(z)

if y == '+':
    a = x + z
    # cryptic looking formatting on the variable to get
    # one decimal place answer
    print(f'{a:.1f}')
elif y == '-':
    a = x - z
    print(f'{a:.1f}')
elif y == '*':
    a = x * z
    print(f'{a:.1f}')
else:
    a = x / z
    print(f'{a:.1f}')
