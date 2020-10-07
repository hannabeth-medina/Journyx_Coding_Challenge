#! /usr/bin/env python

""" Module to obtain features based off specified requirements """

import re
import urllib.request
import json


# Function to extract emoticons in message
def get_emoticons(text):
    return re.findall("\((\w{0,15})\)", text)


# Function to extract mentions in message
def get_mentions(text):
    return re.findall("@(\w+)", text)


# Function to extract url and title for each link in message
def get_links(text):
    # Look for urls
    url_list = re.findall("http\S+", text)

    # If no urls found -> quit early
    if not url_list:
        return None

    link_list = []
    for url in url_list:
        # Only open valid urls
        try:
            html = urllib.request.urlopen(url).read()
        except:
            break
        
        title = re.search("<title>(.*?)</title>", str(html))
        # Add url and current HTML title limited to 200 characters to overall list of links
        link_list.append({"url": url, "title": title.group(1)[:200]})

    return link_list


    """ Methods for additional features can be added here """
