# pseudocode
# input great question tied to a variable
# if answer is 42 etc. print 'yes'
# else print 'no'
# thought later about using 'match'

user_answer = input('What is the answer to the '
                    'Great Question of Life, '
                    'the Universe, of Everything? ').lower().strip()
#  lined up the code above correctly so it can go on 3 lines, pep8

match user_answer:
    case '42' | 'forty-two' | 'forty two':
        print('yes')
    case _:
        print('no')
