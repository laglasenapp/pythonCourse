from flask import Flask, render_template, redirect, request
import os
nome = 'Site Flask 2'

#lista_empresas = ['Proway','Hbsis','T-Systems','Senior','Philips']

dicionario_empresa = {}

firstTime = False

#name - nome do arquivo - sintaxe exigida pelo Flask
app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html', titulo=nome)

@app.route('/empresa')
def empresa():
    global firstTime
    if not firstTime :
        ler_arquivo()
        firstTime = True
    return render_template('empresa.html', titulo=nome, empresas=dicionario_empresa)

@app.route('/bezi')
def bezi():
    return 'O Lubi ama a Bezi '

@app.route('/salvar_empresa', methods = ['POST'])
def salvar_empresa():
    empresa = request.form.get('empresa')
    ti_param = request.form.get('ti')
    ti = ti_param == 'on'
    dicionario_empresa.update({empresa : ti})
    gravar_arquivo()
    return redirect('/empresa')

@app.route('/cadastrar_empresa')
def cadastrar_empresa_tela():
    return render_template('cadastrar_empresa.html')


@app.route('/usuario')
def usuario():
    user = {'username': 'Luiz'}
    return '''
    <html>
        <head>
            <title>Curso de Python - Aula 4</title>
        </head>
        <body>
            <h1>Hello, ''' + user['username'] + '''!</h1>
        </body>
    </html>'''

def  ler_arquivo():
    try:
        with open('dados.txt','r') as arquivo:
            for l in arquivo:
                linha = l.strip()
                array = linha.split(';')
                empresa = array[0]
                ti = array[1]
                dicionario_empresa.update({empresa:ti})
    except Exception as e:
        print(e)
    

def gravar_arquivo():
    try:
        os.remove('dados.txt')
    except:
        print('Arquivo não existe')
    with open('dados.txt','w') as arquivo:
        for x in dicionario_empresa:
            arquivo.write(f'{x};{dicionario_empresa[x]}\n')

app.run(debug=True)