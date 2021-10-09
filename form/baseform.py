from flask_wtf import FlaskForm

class MyBaseForm(FlaskForm):
    class Meta:
        locals = ['zh']