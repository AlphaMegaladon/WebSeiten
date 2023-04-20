from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.config['SECRET_KEY'] = '4413'

@app.route('/')
def start_page():
    return render_template('start_page.html')

@app.route('/WorkExperience/')
def WorkExperience():
    return render_template('Work_Experience.html')

@app.route('/Education/')
def Education():
    return render_template('Education.html')

@app.route('/PublicationsAndProjects/')
def PublicationsAndProjects():
    return render_template('Publications_and_Projects.html')

@app.route('/PersonalInterests/')
def PersonalInterests():
    return render_template('Personal_Interests.html')