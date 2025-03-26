import sys
import os

# Adiciona o caminho do diretório backend ao sys.path para importar o módulo 'app'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
