from flask import Flask, render_template, request
from Config import config

app = Flask(__name__)
app.config.from_object(config)

# app.config['STATIC_FOLDER'] = '..\tatic'
# app.config['STATIC_URL_PATH'] = 'static'
# app.config["DEVELOPMENT"] = True
# app.config['DEBUG'] = True

@app.route('/homepage')
def homepage():
    return render_template("homepage.html")

@app.route('/index',methods=['GET','POST'])
def index(name=None):
    if request.method == 'GET' and request.method == 'POST':
        pass

@app.route('/longin',methods=['GET','POST'])
def longin(name=None):
    if request.method == "GET":
        return render_template('longin.html')
    elif request.method == "POST":
        pass
    else:
        pass