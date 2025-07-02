from app import app
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
    
    if request.method == 'GET':
        pesquisa = request.args.get('pesquisa')
        print('GET:', pesquisa)
        context.update({'pesquisa':pesquisa})
        
    if request.method == 'POST':
        pesquisa = request.form['pesquisa']
        print('POST:', pesquisa)
        context.update({'pesquisa':pesquisa})
    
    return render_template('contato.html', context=context)