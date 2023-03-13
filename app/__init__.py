# Estou importando a classe "Flask" para que eu possa utilizar o framework
from flask import Flask

# Estou importando a classe "SQLalchemy" do módulo "flask_sqlalchemy"
from flask_sqlalchemy import SQLalchemy


# Define a minha aplicação
app = Flask(__name__)

# É uma configuração: é a URL de conexão a URI de conexão com o Banco De Dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db'

# Estou instanciando a classe SQLalchemy do módulo flask_sqlalchemy
db = SQLalchemy(app)

# A importação está sendo feita longe do início porque precisamos que informações dos controllers
# e models sejam importados logo depois da variável da aplicação (app) esteja declarada
from app.controllers import default


