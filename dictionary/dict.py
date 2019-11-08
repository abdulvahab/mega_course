#!/usr/bin/env python
'''This app takes a word from user and returened the dictionary mening of that word'''
import json
from difflib import get_close_matches
file = open("data.json")
data = json.load(file)
def get_meaning(word):
    word = word.lower()
    if word in data.keys():
        result = "\n".join(meaning for meaning in data[word])
        return f'\n{result}\n'
    else:
        new_word = get_close_matches(word,data.keys(),cutoff=0.8)[0]
        if word:
            choice = input(f'The {word} not in dictionary, Do you mean {new_word},(Y or N)? : ')
            if choice.lower() == 'y':
                result = "\n".join(meaning for meaning in data[new_word])
                return f'\n{result}\n'
            else:
                return "The word doesn't found, please check and re-enter"
if __name__=="__main__":
    while True:
        word = input("Enter your word or '0' to exit: ")
        if word == '0':
            print("Than for using dictionary app, see you again\n")
            exit()
        print(get_meaning(word))
