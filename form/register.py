from form.baseform import MyBaseForm
from wtforms import TextField, StringField, PasswordField, BooleanField, SubmitField, IntegerField, widgets
from wtforms.validators import DataRequired, EqualTo
from flask_wtf import RecaptchaField


class RegisterForm(MyBaseForm):
    username = StringField('账号', validators=[DataRequired()])
    password = PasswordField('密码', validators=[DataRequired()], widget=widgets.PasswordInput())
    password1 = PasswordField('确认密码', validators=[DataRequired(), EqualTo('password', message=u'两次密码不一致')],
                              widget=widgets.PasswordInput())
    name = StringField('姓名', validators=[DataRequired()])
    department = StringField('部门', validators=[DataRequired()])
    drivingLicence_number = IntegerField('驾驶证编号', validators=[DataRequired()])
    phone_number = IntegerField('手机号', validators=[DataRequired()])
    # recaptcha = RecaptchaField()
    submit = SubmitField('提交')
