from parse_chat import parse_chat

print('This program uses the parse_chat function to parse your input.')
print('You may quit by typing "quit".\n')

message = ''

while message != 'quit':
    message = input('Chat: ')
    
    if message != 'quit':
        print(parse_chat(message))
    