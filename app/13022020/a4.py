from flask import Flask, render_template

nome = 'Site Flask 2'

lista_empresas = ['Proway','Hbsis','T-Systems','Senior','Philips']

#name - nome do arquivo - sintaxe exigida pelo Flask
app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html', titulo=nome)

@app.route('/empresa')
def empresa():
    return render_template('empresa.html', titulo=nome, empresas=lista_empresas)

@app.route('/bezi')
def bezi():
    return 'O Lubi ama a Bezi '

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

app.run(debug=True)