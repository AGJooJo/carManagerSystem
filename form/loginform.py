from form.baseform import MyBaseForm
from wtforms import TextField,StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired

class LoginForm(MyBaseForm):
    username = StringField('username',validators=[DataRequired(message=u'名字不能为空')])
    password = PasswordField('password',validators=[DataRequired(message=u'密码不能为空')])
    remember = BooleanField('remember me')
    submit = SubmitField('login in')