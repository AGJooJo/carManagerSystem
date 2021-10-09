from flask import Flask, render_template, request, redirect, url_for, Response
from Config import config
from form.loginform import LoginForm
from form.register import RegisterForm
from gmssl import sm2,utils
from tool import secretkey

app = Flask(__name__)
app.config.from_object(config)
# app.config['STATIC_FOLDER'] = '..\tatic'
# app.config['STATIC_URL_PATH'] = 'static'
# app.config["DEVELOPMENT"] = True
# app.config['DEBUG'] = True


@app.route('/register',methods=['GET','POST'])
def register(name='register'):
    form = RegisterForm()
    resp = Response()
    secretkey_sm = secretkey()
    if form.validate_on_submit() and secretkey_sm.get_pubkey() == request.cookies['psw_sm']:
        print(request.cookies['psw_sm'])
        print(form.data)
        return redirect(url_for('login'), code=302)
    resp.data = render_template('register.html',form=form)
    resp.set_cookie('psw_sm',secretkey_sm.get_pubkey())
    return resp

@app.route('/',methods=['GET'])
@app.route('/login',methods=['GET','POST'])
def login(name=None):
    form = LoginForm()
    if request.method == "GET":
        return render_template('login.html',form=form)
    # elif request.method == "POST" and form.validate():
    elif form.validate_on_submit():
        return 'nihao'
    else:
        pass


@app.route('/homepage')
def homepage():
    return render_template("homepage.html")

@app.route('/index',methods=['GET','POST'])
def index(name=None):
    if request.method == 'GET' and request.method == 'POST':
        pass