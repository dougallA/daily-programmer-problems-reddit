"""
Description:

We know arrays. We index into them to get a value. What if we could apply this to a string? But the index finds a "word". Imagine being able to parse the words in a string by giving an index. This can be useful for many reasons.

Example:

Say you have the String "The lazy cat slept in the sunlight."

If you asked for the Word at index 3 you would get "cat" back. If you asked for the Word at index 0 you get back an empty string "". Why an empty string at 0? Because we will not use a 0 index but our index begins at 1. If you ask for word at index 8 you will get back an empty string as the string only has 7 words. Any negative index makes no sense and return an empty string "".
Rules to parse:

    Words is defined as [a-zA-Z0-9]+ so at least one of these and many more in a row defines a word.
    Any other character is just a buffer between words."
    Index can be any integer (this oddly enough includes negative value).
    If the index into the string does not make sense because the word does not exist then return an empty string.

Challenge Input:

Your string: "...You...!!!@!3124131212 Hello have this is a --- string Solved !!...? to test @\n\n\n#!#@#@%$**#$@ Congratz this!!!!!!!!!!!!!!!!one ---Problem\n\n"

Find the words at these indexes and display them with a " " between them: 12 -1 1 -100 4 1000 9 -1000 16 13 17 15
"""
import re

def string_index(sentence, index_number):
    pattern = re.compile(r'[^a-zA-Z0-9]+')
    word_list = re.split(pattern, sentence)
    if 0 < index_number < len(word_list)+1:
        return word_list[index_number - 1]
    else:
        return ""

if __name__ == '__main__':
    print string_index(raw_input('Enter a sentence: '), int(raw_input('Enter an index: ')))
