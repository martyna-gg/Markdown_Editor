global text

# menu
decisions = ['plain', 'bold', 'italic', 'header', 'link', 'inline-code', 'new-line', 'ordered-list', 'unordered-list', '!help', '!done']

decision = ''
text = ''

# functions for menu positions
def plain():
    global text
    text += input('Text: >') + ' '
    print(text)

def bold():
    global text
    text += '**' + input('Text: >') + '** '
    print(text)

def italic():
    global text
    text += '*' + input('Text: >') + '* '
    print(text)

def header():
    global text
    level = int(input('Level: >'))
    try:
        while level not in range(1,7):
            print('The level should be within the range of 1 to 6')
            level = int(input('Level: >'))
    except ValueError:
            print('The level should be within the range of 1 to 6')
            level = int(input('Level: >'))

    text += '\n' + '#' * level + ' ' + input('Text: >') + '\n'
    print(text)

def link():
    global text
    label = input('Label: >')
    URL = input('URL: >')
    text += f'[{label}]({URL}) '
    print(text)

def inline_code():
    global text
    text += '`' + input('Text: >') + '` '
    print(text)

def new_line():
    global text
    text += '\n'
    print(text)

def list(type_of_list):
    global text
    rows = input('Number of rows: >')
    try:
        while int(rows) < 1:
            print('The number of rows should be greater than zero')
            rows = input('Number of rows: >')
    except ValueError:
            print('The number of rows should be greater than zero')
            rows = input('Number of rows: >')

    text += '\n'

    for x in range(1, int(rows) + 1):
        if type_of_list == 'ordered-list':
            text += f'{x}. ' + input(f'Row #{x}: >') + '\n'
        else:
            text += '*' + input(f'Row #{x}: >') + '\n'
    print(text)

# decisions loop        
while decision != '!done':
    decision = input('Choose a formatter, type !help for displaying menu or !done for saving your file and exit: >')
    if decision not in decisions:
        print('Unknown formatting type or command')
    if decision == '!help':
        print('Available formatters: ' + ' '.join(decisions[0:-2]))
        print('Special commands: ' + ' '.join(decisions[-2::]))
    if decision == 'plain':
        plain()
    if decision == 'bold':
        bold()
    if decision == 'italic':
        italic()
    if decision == 'header':
        header()
    if decision == 'link':
        link()
    if decision == 'inline-code':
        inline_code()
    if decision == 'new-line':
        new_line()
    if decision == 'ordered-list':
        list(decision)
    if decision == 'unordered-list':
        list(decision)

# saving the text in a file            
text_file = open('./output.md', 'w')
text_file.write(text)
text_file.close()
