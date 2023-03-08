from app import app
# Do módulo "app" estou importando a variável "app"



# A página principal da aplicação
@app.route("/")
def index():
    return "página principal"



