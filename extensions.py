'''
pseudocode
1. prompt user for name of file e.g. 'cat.gif ' tie that to variable
use methods .lower() and .strip() for edge cases
2. if file extension name is '.gif .jpg .jpeg .png .pdf .txt .zip'
output appropriate response like 'media/gif' check mozilla
3. else output 'application/octet-stream'
'''

user_input = input('Type in filename with extension: ').lower().strip()

if user_input.endswith('.gif'):
    # initially made the mistake of adding
    # 'if user_input == user_input.ends...' but the new
    # statement checks for truthiness by itself
    # user_input does NOT equal the user_input with the method attached
    # i always got the else code returned because of that
    print('image/gif')
elif user_input.endswith('.jpg'):
    print('image/jpeg')
elif user_input.endswith('.jpeg'):
    print('image/jpeg')
elif user_input.endswith('.png'):
    print('image/png')
elif user_input.endswith('.pdf'):
    print('application/pdf')
elif user_input.endswith('.txt'):
    print('text/plain')
elif user_input.endswith('.zip'):
    print('application/zip')
else:
    print('application/octet-stream')
