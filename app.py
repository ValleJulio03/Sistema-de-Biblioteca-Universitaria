from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api
from models import db
from controllers.usuario_controller import usuario_ns

# Inicializar Flask y configuraciones
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///biblioteca.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar SQLAlchemy y registrar la API
db.init_app(app)
api = Api(app, title="Sistema de Biblioteca", version="1.0", description="API para gestionar la biblioteca")

# Registrar namespaces
api.add_namespace(usuario_ns, path="/usuarios")

# Crear tablas
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
