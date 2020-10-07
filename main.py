 #! /usr/bin/env python

""" Module to obtain information about chat message content """

import sys
from features import *


def main(input):
    """ Takes in chat message string as input, returns JSON formatted string with information about its contents """
    
    # Ensure input is valid string
    if type(input) != str:
        return "Not valid string input"
    
    result = {}

    # Total word count
    count = len(input.split())

    """ Additional features can be added to this list """
    features = ["emoticons", "mentions", "links"]

    # For each feature in list call respective function to retrieve values
    for feature in features:
        feature_list = getattr(sys.modules[__name__], "get_{}".format(feature))(input)
        if feature_list:
            result[feature] = feature_list
            count -= len(feature_list)

    # Word count not including features
    result["words"] = count

    # Format dictionary to JSON formatted string
    return json.dumps(result, indent=2)



if __name__ == "__main__":
    # print(main("@john hey, you and @emily around?"))
    print(main("@mary @john (success) such a cool feature! Check this out: https://journyx.com/features-and-benefits/data-validation-tool"))
    # print(main("The World Series is starting soon! (cheer) https://www.mlb.com/ and https://espn.com"))
    # print(main("Good morning! (smile) (coffee)"))
    # print(main(3))