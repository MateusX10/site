# Estou importando a classe "Flask" para que eu possa utilizar o framework
from flask import Flask



# Define a minha aplicação
app = Flask(__name__)



# A página principal da aplicação
@app.route("/")
def index():
    return "página principal"



# A aplicação será executada somente se o usuário estiver executando o arquivo principal e não um secundário
if __name__ == "__main__":
    app.run(debug=True)

