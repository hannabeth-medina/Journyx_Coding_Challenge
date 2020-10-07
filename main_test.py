 #! /usr/bin/env python

from trial import *
import unittest


class TestInsights(unittest.TestCase):
    def test_emoticons(self):
        # Test 1: base case (only alpha)
        self.assertEqual(get_emoticons("@mary @john (success) such a cool feature! Check this out: https://journyx.com/features-and-benefits/data-validation-tool"), ["success"])
        # Test 2: contains digit
        self.assertEqual(get_emoticons("The World Series is starting soon! (cheerx3) https://www.mlb.com/ and https://espn.com"), ["cheerx3"]) 
        # Test 3: contains non-alphanumeric
        self.assertEqual(get_emoticons("The World Series is starting soon! (cheers,)"), [])         
        # Test 4: whitespace inside parentheses
        self.assertEqual(get_emoticons("Good morning! (smile) (coffee) (this has whitespaces in it) ( smileagain) "), ["smile", "coffee"])
        # Test 5: longer than 15 characters
        self.assertEqual(get_emoticons("Good morning! (smile) (coffee) (thisislongerthan15characters)"), ["smile", "coffee"])

    def test_mentions(self):
        # Test 1: base case (only alpha)
        self.assertEqual(get_mentions("@mary @john (success) such a cool feature! Check this out: https://journyx.com/features-and-benefits/data-validation-tool"), ["mary", "john"])
        # Test 2: only digits and underscore
        self.assertEqual(get_mentions("Hello this is testing @_123_"), ["_123_"])
        # Test 3: ends with non-word character that's not whitespace
        self.assertEqual(get_mentions("This ends with a comma @comma,"), ["comma"])
        # Test 4: empty mentions
        self.assertEqual(get_mentions("No mentions resulting from @ @@ @@!"), [])
    
    def test_links(self):
        # Test 1: base case
        self.assertEqual(get_links("This is the link for https://www.python.org/"), [{"url": "https://www.python.org/", "title": "Welcome to Python.org"}])
        # Test 2: multiple links
        self.assertEqual(get_links("this is link 1 and 2 https://www.youtube.com/ https://search.yahoo.com/search?p=yahoo&fr=yfp-t&ei=UTF-8&fp=1"), [{"url": "https://www.youtube.com/", "title": "YouTube"}, {"url": "https://search.yahoo.com/search?p=yahoo&fr=yfp-t&ei=UTF-8&fp=1", "title": "yahoo - Yahoo Search Results"}])
        # Test 3: contains invalid link
        self.assertEqual(get_links("This link is not a real link https://notareallink.com"), [])

    def test_main(self):
        # Test 1: non-string input
        self.assertEqual(main(678), "Not valid string input")
        

        

if __name__ == "__main__":
    unittest.main(verbosity=2)
