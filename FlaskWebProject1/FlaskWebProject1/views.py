"""
Routes and views for the flask application.
"""
#Here I import everything that I need for the python programming
from datetime import datetime
from FlaskWebProject1.Models.LocalDatabaseRoutines import create_LocalDatabaseServiceRoutines
from flask import render_template
from FlaskWebProject1 import app
from os import path
from datetime import datetime
from flask import render_template, redirect, flash, request
from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from FlaskWebProject1.Models.forms import ExpandForm
from FlaskWebProject1.Models.forms import CollapseForm 
from FlaskWebProject1.Models.forms import LoginFormStructure
from FlaskWebProject1.Models.forms import RegisterFormStructure
from FlaskWebProject1.Models.forms import QueryForm
from os import path
from flask_bootstrap import Bootstrap
bootstrap = Bootstrap(app)
db_Functions = create_LocalDatabaseServiceRoutines() 
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import io
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas



import pandas as pd
app.config['SECRET_KEY'] = 'bla bla'
#These are all the routes. Each route creates a separate page for my website.
@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',   
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Contact Page'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='About my project'
    )

@app.route('/Data')
def Data():
    return render_template(
        'data.html',
        title = 'Data',
         year=datetime.now().year,
        message=''
        )
@app.route('/Contact')
def Contact():
    return render_template(
        'contact.html',
        title = 'Contact',
         year=datetime.now().year,
        message='Contact Us'
        )

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginFormStructure(request.form)

    #This checks to see if the log in was correct. If it is, it will redirect user to query page, while if incorrect it will tell the user that it entered wrong credentials.
    if (request.method == 'POST'):
        if (db_Functions.IsLoginGood(form.username.data, form.password.data)):
            return redirect('/query')
        else:
            flash('Error: Wrong Cerdentials!')
   
    return render_template(
        'login.html',
        form=form, 
        title='Login',
        year=datetime.now().year,
        repository_name='Pandas'
    )

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterFormStructure(request.form)

    #this asks the backend to check to see if the user has already been created. If it was, it will say so, and if it was it will add the new user.
    if (request.method == 'POST'):
        if (not db_Functions.IsUserExist(form.username.data)):
            db_Functions.AddNewUser(form)
            db_table = ""
            return redirect('/')
        else:
            flash('Error: User Exists!')
            form = RegisterFormStructure(request.form)
    return render_template(
        'register.html',
        form=form,
        title='Register',
        year=datetime.now().year,
        repository_name='Pandas'
    )
@app.route('/massShootings', methods=['GET', 'POST'])
def massShootings():
    #this helps me check to see if the website has problems reading the file
        form1 = ExpandForm()
        form2 = CollapseForm()
        df = pd.read_csv(path.join(path.dirname(__file__), 'static/data/MassShootingsShort.csv'))
        raw_data_table = ''

        #this is the expand and collapse functions
        if request.method == 'POST':
            if request.form['action'] == 'Expand' and form1.validate_on_submit():
               raw_data_table = df.to_html(classes = 'table table-hover')
            if request.form['action'] == 'Collapse' and form2.validate_on_submit():
               raw_data_table = ''

        return render_template(
        'massShootings.html',
        title = 'MassShootings',
         year=datetime.now().year,
        message='Mass Shootings',
        form1 = form1,
        form2 = form2,
        raw_data_table = raw_data_table
        )



@app.route('/homicides', methods=['GET', 'POST'])
def homicides():
    #this helps me check to see if the website has problems reading the file
        form1 = ExpandForm()
        form2 = CollapseForm()
        print("starting to read csv ... ")
        df = pd.read_csv(path.join(path.dirname(__file__), 'static/data/homicidesShort.csv'), encoding = "utf-8", low_memory = False)
        print("Done reading csv ")
        raw_data_table = ''

        #this is the expand and collapse functions
        if request.method == 'POST':
            if request.form['action'] == 'Expand' and form1.validate_on_submit():
                print("try to expand ")
                raw_data_table = df.to_html(classes = 'table table-hover')
                print("done converting to html")
            if request.form['action'] == 'Collapse' and form2.validate_on_submit():
               raw_data_table = ''

        return render_template(
        'homicides.html',
        title = 'Homicides',
         year=datetime.now().year,
        message='Homicides',
        form1 = form1,
        form2 = form2,
        raw_data_table = raw_data_table
        )


@app.route('/usPresidents', methods=['GET', 'POST'])
def usPresidents():

        form1 = ExpandForm()
        form2 = CollapseForm()
        df = pd.read_csv(path.join(path.dirname(__file__), 'static/data/us_presidents.csv'), encoding = "utf-8")
        raw_data_table = ''

        if request.method == 'POST':
            if request.form['action'] == 'Expand' and form1.validate_on_submit():
               raw_data_table = df.to_html(classes = 'table table-hover')
            if request.form['action'] == 'Collapse' and form2.validate_on_submit():
               raw_data_table = ''
     
        return render_template(
        'usPresidents.html',
        title = 'usPresidents',
         year=datetime.now().year,
        message='US Presidents',
        form1 = form1,
        form2 = form2,
        raw_data_table = raw_data_table

            )


@app.route('/stateElections', methods=['GET', 'POST'])
def stateElections():
        form1 = ExpandForm()
        form2 = CollapseForm()
        df = pd.read_csv(path.join(path.dirname(__file__), 'static/data/election_resultsSHORT.csv'), encoding = "utf-8", low_memory = False)
        raw_data_table = ''

        if request.method == 'POST':
            if request.form['action'] == 'Expand' and form1.validate_on_submit():
               print("Converting to html")
               raw_data_table = df.to_html(classes = 'table table-hover')
               print("done")
            if request.form['action'] == 'Collapse' and form2.validate_on_submit():
               raw_data_table = ''
     

        return render_template(
        'stateElections.html',
        title = 'stateElections',
         year=datetime.now().year,
        message='State Elections',
        form1 = form1,
        form2 = form2,
        raw_data_table = raw_data_table

            )



@app.route('/query' , methods = ['GET' , 'POST'])
def query():


    form1 = QueryForm()
    chart = ''

   #reading the data file then selecting a few choices for categories and saving it to a variable.
    df = pd.read_csv(path.join(path.dirname(__file__), 'static/Data/MassShootingsShort.csv'))
    category_list = ['Cause' , 'Gender' , 'Age' , 'Target' , 'Race' , 'Mental Health Issues']
    category_choices = list(zip(category_list,category_list))
    form1.category.choices = category_choices

    #this will group the data into the chosen categories and creat a bar chart that shows the selected one.
    if request.method == 'POST':
        category = form1.category.data
        df = df[[category]]
        df = df.groupby(category).size()
        fig = plt.figure()
        ax = fig.add_subplot(111)
        fig.subplots_adjust(bottom=0.4)
        df.plot(kind = 'bar', ax = ax)
        chart = plot_to_img(fig)

    
    return render_template(
        'query.html',
        form1 = form1,
        chart = chart

    )
#Here function for showing the charts that I make with the queries
def plot_to_img(fig):
    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)
    pngImageB64String = "data:image/png;base64,"
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')
    return pngImageB64String

        

