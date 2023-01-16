#!/usr/bin/python3
"""
This function contains text_indentation function
"""


def text_indentation(text):
    """
    This function prints a text with 2 new lines
    after each of these characters: ., ? and :
    Arguments:
        @text: The Text to be modify
    """
    if type(text) != str:
        raise TypeError('text must be a string')

    ind = 0
    for word in text:
        if word in '.?:' or word == '\n':
            print(word)
            print()
            ind += 1
        elif text[ind - 1] in '.?:' and word == " ":
            print("", end="")
            ind += 1
        else:
            print(word, end="")
            ind += 1
