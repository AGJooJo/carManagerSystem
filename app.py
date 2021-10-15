from flask import Flask, render_template, request, redirect, url_for, Response
from Config import config
from form.loginform import LoginForm
from form.register import RegisterForm
from tool import Secretkey
from gmssl.sm2 import CryptSM2

app = Flask(__name__)
app.config.from_object(config)
# app.config['STATIC_FOLDER'] = '..\tatic'
# app.config['STATIC_URL_PATH'] = 'static'
# app.config["DEVELOPMENT"] = True
# app.config['DEBUG'] = True

def decrypt_sm2(prikey,request):
    cryptsm2 = CryptSM2(public_key=None,private_key=prikey)
    dict_content = request.get_json()
    dict_decrypt_content = dict()
    for d in dict_content:
        data_median_cuphertext = dict_content[d].encode(encoding = "ascii")
        print(dict_content[d])
        print(type(dict_content[d]))
        print(data_median_cuphertext)
        print(type(data_median_cuphertext))
        # data_median_plainttext = cryptsm2.decrypt(dict_content[d])
        data_median_plainttext = cryptsm2.decrypt(data_median_cuphertext)
        print(data_median_plainttext)
        data_plaintext = data_median_plainttext.decode(encoding = "utf-8")
        dict_decrypt_content[d] = data_plaintext
    return dict_decrypt_content

@app.route('/register',methods=['GET','POST'])
def register(name='register'):
    form = RegisterForm()
    resp = Response()
    secretkey_sm = Secretkey()
    # if form.validate_on_submit() and secretkey_sm.get_pubkey() == request.cookies['psw_sm']:
    if request.method == "POST" and secretkey_sm.get_pubkey() == request.cookies['psw_sm']:
        prikey = secretkey_sm.get_prikey()
        dict_decrypt_content = decrypt_sm2(prikey,request)
        print(dict_decrypt_content)
        # return redirect(url_for('login'), code=302)
    secretkey_sm.set_key()
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


if __name__ == '__main__':
    app.run("192.168.255.128",5000)