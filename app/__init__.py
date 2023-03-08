# Estou importando a classe "Flask" para que eu possa utilizar o framework
from flask import Flask



# Define a minha aplicação
app = Flask(__name__)

# A importação está sendo feita longe do início porque precisamos que informações dos controllers
# e models sejam importados logo depois da variável da aplicação (app) esteja declarada
from app.controllers import default


