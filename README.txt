This program contains the function parse_chat(message) that returns JSON containing all mentions, emoticons, and
links in the message. A count of all non-feature words is also included in the JSON string.

# Mentions always begin with '@' and are followed by 1 or more word
#     characters
# Links are designated by a space or the beginning of the line,
#     followed by 'http', followed by any number of non-whitespace
#     characters
# Emoticons always begin with '(' and end with ')', with 1-15 word
#     characters between the parenthesis

The word count represents the number of non-feature words in the string. If a feature separates two groups of
characters, those two groups are counted as separate words. For example, the string:

'123(abc)456'

Would count as one emoticon: '(abc)' and two words: '123' and '456'.

A chat.py script is included that runs the parse_chat function on user input and displays the output.