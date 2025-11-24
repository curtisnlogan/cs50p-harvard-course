# psuedocode
# input get user greeeting methods .strip().lower()
# if user input is 'hello' print '$0'
# if user input starts with 'h' but not 'hello' print '$20'
# else output '$100'

user_greeting = input('Enter a greeting: ').lower().strip()

if user_greeting.startswith('hello'):
    print('$0')
elif user_greeting[0] == 'h' and not user_greeting.startswith('hello'):
    # accessed the first letter of this variable with square brackets
    # 'boolean operators 'and not' to
    # check it also doesn't start with hello
    # .startswith method found through exploring documentation
    print('$20')
else:
    print('$100')
