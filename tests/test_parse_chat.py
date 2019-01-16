import unittest
from parse_chat import parse_chat

class TestParseChat(unittest.TestCase):

    def test_word_count_no_features(self):
        result = parse_chat("Hello world")
        self.assertEqual(result, '{"words": 2}')
    
    def test_word_count_no_features_no_words(self):
        result = parse_chat("")
        self.assertEqual(result, '{"words": 0}')
    
    def test_mention(self):
        result = parse_chat("@mention1")
        self.assertEqual(result, '{"words": 0, "mentions": ["mention1"]}')
    
    def test_mention_with_word(self):
        result = parse_chat("foo@bar")
        self.assertEqual(result, '{"words": 1, "mentions": ["bar"]}')
        
    def test_mention_in_parentheses(self):
        result = parse_chat("(@foo)")
        self.assertEqual(result, '{"words": 2, "mentions": ["foo"]}')
        
    def test_mention_with_link(self):
        result = parse_chat("@http")
        self.assertEqual(result, '{"words": 0, "mentions": ["http"]}')
        
    def test_emoticon(self):
        result = parse_chat("(foo)")
        self.assertEqual(result, '{"words": 0, "emoticons": ["foo"]}')
    
    def test_emoticon_with_space(self):
        result = parse_chat("(foo bar)")
        self.assertEqual(result, '{"words": 2}')
    
    def test_emoticon_with_link(self):
        result = parse_chat("(http)")
        self.assertEqual(result, '{"words": 0, "emoticons": ["http"]}')
    
    def test_emoticon_max_length(self):
        result = parse_chat("(123456789012345)")
        self.assertEqual(result, '{"words": 0, "emoticons": ["123456789012345"]}')
    
    def test_emoticon_too_long(self):
        result = parse_chat("(1234567890123456)")
        self.assertEqual(result, '{"words": 1}')
        
    def test_emoticon_min_length(self):
        result = parse_chat("(1)")
        self.assertEqual(result, '{"words": 0, "emoticons": ["1"]}')
        
    def test_emoticon_too_short(self):
        result = parse_chat("()")
        self.assertEqual(result, '{"words": 1}')
    
    def test_link(self):
        result = parse_chat("http://www.google.com")
        self.assertEqual(result, '{"words": 0, "links": [{"url": "http://www.google.com", "title": "Google"}]}')

    def test_bad_link(self):
        result = parse_chat("httpfoo")
        self.assertEqual(result, '{"words": 0, "links": [{"url": "httpfoo", "title": null}]}')

if __name__ == '__main__':
    unittest.main()