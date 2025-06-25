from app import app
from flask import render_template

@app.route('/')
def homepage():
    user = 'Gabriel'
    age = 17
    
    context = {
        'user':user,
        'age':age
    }
    
    return render_template('index.html', context=context)

@app.route('/itsok')
def novapagina():
    user = 'Gabriel'
    
    context = {
        'user':user
    }
    
    return render_template('itsok.html', context=context)
