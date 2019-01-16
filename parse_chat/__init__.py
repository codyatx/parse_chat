import json
import urllib
import re

def parse_chat(message):
    """
    Returns a JSON string containing information about the contents of a chat
    message, including:
        @mentions
        URLs, as well as page titles up to 200 characters
        (emoticons)
        Word count of words that do not meet the requirements above
    """
    
    
    result = {
        "words": 0
    }
    index = 0
    cont = True
    
    # Begin at the start of the word. At the first occurence of any feature,
    # process that feature and then continue at the next character after that
    # feature
    while cont:
        # RE rules for finding features:
        # Mentions always begin with '@' and are followed by 1 or more word
        #     characters
        # Links are designated by a space or the beginning of the line,
        #     followed by 'http', followed by any number of non-whitespace
        #     characters
        # Emoticons always begin with '(' and end with ')', with 1-15 word
        #     characters between the parenthesis
        match = re.search('(@\w+|(\A|\s)http\S*|\(\w{1,15}\))', message[index:])
        
        # If any feature is matched, the loop continues.
        if match:
            feature = match.group(1)                    # The feature string found by the RE
            location = message.find(feature, index)     # Index of the feature string
            left = message[index:location]              # String containing all chars between the current index and the feature's index
            index = location + len(feature)             # New index value, the loop runs again starting at the first char after the feature
            result["words"] += len(left.split())        # Increments the word count.
            
            # Code to process the 'mention' feature
            if feature[0] == '@':
                mention = feature[1:]
                
                if "mentions" in result:
                    result["mentions"].append(mention)
                else:
                    result["mentions"] = [mention]
            
            # Code to process the 'emoticon' feature
            elif feature[0] == '(':
                emoticon = feature[1:-1]
            
                if "emoticons" in result:
                    result["emoticons"].append(emoticon)
                else:
                    result["emoticons"] = [emoticon]
            
            # Code to process the 'link' feature
            else:
                feature = feature.lstrip()
                title = _get_title(feature)
                link = {
                    "url": feature,
                    "title": title
                }
                
                if "links" in result:
                    result["links"].append(link)
                else:
                    result["links"] = [link]
            
            
        # If a match wasn't found, end the loop by counting the remaining words
        else:
            result["words"] += len(message[index:].split())
            cont = False
    
    # Convert to JSON and return
    return json.dumps(result)
    

def _get_title(url):
    """
    Given a URL, returns the title of the webpage. Returns nothing if the URL
    is not valid.
    """
    
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read()
            match = re.search('<title>(.*?)</title>', html.decode('ascii', errors='ignore'))
            title = match.group(1) if match else ''
            return title[:200]
    except ValueError:
        return