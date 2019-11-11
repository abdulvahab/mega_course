from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class WordForm(FlaskForm):
    word = StringField('Enter your Word',
                        validators=[DataRequired()]
                      )
    submit = SubmitField('Get meaning')
class AlternateWordForm(FlaskForm):
    word = SelectField('Choose alternate word', choices=[], validators=[DataRequired()])
    submit = SubmitField('Use this word')
    
    '''
    def __init__(self,alt_words,choices=[]):
        self.alt_words = alt_words
        self.choices = choices
        for alt_word in self.alt_words:
            self.choices.append((alt_word,alt_word))
        word = SelectField('alt_word', choices=self.choices)
    '''