from flask import Flask, request
import mysql.connector 

app = Flask(__name__)

# create a MySQL connection
cnx = mysql.connector.connect(
    host="sql10.freesqldatabase.com",
    user="sql10604688",
    password="94DvzhSSM4",
    database="sql10604688"
)

@app.route('/login/<email>/<senha>', methods=['GET', 'POST'])
def login(email, senha):
    #if request.method == 'POST':
    cursor = cnx.cursor()
    query = "SELECT * FROM usuario_plataforma WHERE email = 'gustavos@gmail.com' and senha = 'senhaakls'"
    cursor.execute(query)
    result = cursor.fetchone()
    #verificar se usuário existe ou não existe
    #se usuário existir retornar os dados do usuário
    if(result):
                return {
            'message': 'Usuário não encontrado',
            'status': '404'
        }

    else:

            return {
            'message': 'Usuário encontrado',
            'status': '202'
        }


@app.route('/register/<email>/<senha>')
def register():
    #verificar se o usuário já existe se sim retornar erro
    #se usuário ainda não existir efetuar cadastro
    return 'Hello, !'


#@app.route('/usuario/<usuario>/<senha>')
#def get_users(usuario, senha):
 #   cursor = cnx.cursor()
  #  query = "SELECT * FROM usuario_plataforma WHERE usuario = {usuario} and senha = {senha}"
   # cursor.execute(query)
    #result = cursor.fetchall()
    #return str(result)

@app.route('/create_user')
def create_user():
    cursor = cnx.cursor()
    query = "INSERT INTO usuario_plataforma (nome, sobrenome, cpf, email, senha) VALUES ('Gustavo', 'Queiroz', '0201', 'gustavo@gmail.com', 'senhaakls')"
    cursor.execute(query)
    cnx.commit()
    cursor.close()
    return 'User created successfully!'

app.run()
