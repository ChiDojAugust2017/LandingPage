from flask import Flask, session, request, redirect, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def ninja():
    return render_template('ninja.html')

@app.route('/dojos/new')
def dojonew():
    return render_template('dojonew.html')


app.run(debug=True)