from app import app, db
from flask import render_template, url_for, request
from app.forms import ContatoForm

@app.route('/')
def homepage():
    user = 'Gabriel'
    age = 17
    
    context = {
        'user':user,
        'age':age
    }
    
    return render_template('index.html', context=context)

'''
@app.route('/itsok')
def novapagina():
    user = 'Gabriel'
    
    context = {
        'user':user
    }
    
    return render_template('itsok.html', context=context)
'''

@app.route('/contato/', methods=['GET', 'POST'])
def contato():
    form = ContatoForm()
    context = {}
    
    if form.validate_on_submit():
        form.save()
        
    return render_template('contato.html', context=context, form=form)