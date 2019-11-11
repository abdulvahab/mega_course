#!/usr/bin/env python
'''This app takes a word from user and returened the dictionary meaning of that word'''

import json
from difflib import get_close_matches
from flask import Flask, render_template, url_for, redirect, request
from forms import WordForm, AlternateWordForm
app = Flask(__name__)
app.config['SECRET_KEY'] = "001786" 

file = open("data.json")
data = json.load(file)

@app.route("/", methods=["GET", "POST"])
@app.route("/home",methods=["GET", "POST"])
def home():
    form = WordForm()
    if form.validate_on_submit():
        word = form.word.data.lower()
        return redirect(url_for("meaning", word=word))
    
    return render_template("index.html", title="home", form=form)

@app.route("/meaning/<word>", methods=["GET", "POST"])
def meaning(word):
    alt_form = AlternateWordForm()
    alt_words=None
    result= ["The word doesn't found, please check and re-enter"] 
    if word not in data.keys():
        alt_words = get_close_matches(word,data.keys(),cutoff=0.8)
        if alt_words:
            for alt_word in alt_words:
                alt_form.word.choices.append((alt_word, alt_word))
            if alt_form.validate_on_submit():
                word = alt_form.word.data
                return redirect(url_for("meaning", word=word))
    else:
        result = data[word] 
 
    return render_template("meaning.html", 
                            meanings=result, 
                            word=word, 
                            alt_words=alt_words, 
                            title='meaning',
                            form=alt_form
                        )
if __name__=="__main__":
    app.run(debug=True)
    
    
    '''while True:
        word = input("Enter your word or '0' to exit: ")
        if word == '0':
            print("Thanks for using dictionary app, see you again\n")
            exit()
        print(get_meaning(word))'''
    '''else:
        new_word = get_close_matches(word,data.keys(),cutoff=0.8)[0]
        if word:
            choice = input(f'The {word} not in dictionary, Do you mean {new_word},(Y or N)? : ')
            if choice.lower() == 'y':
                result = "\n".join(meaning for meaning in data[new_word])
                return f'\n{result}\n' '''