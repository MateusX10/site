# Importa a minha aplicação do módulo "app"
from app import app


# A aplicação somente será executada se o usuário estiver rodando a  aplicação através do arquivo principal de execução
if __name__ == "__main__":
    app.run(debug=True)


