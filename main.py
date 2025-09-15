from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from extensions.database import db
from config import Config
from app.routes.auth import auth_bp
from app.routes.chat import chat_bp
from app.routes.message import message_bp
from app.routes.upload import upload_bp

app = Flask(__name__)
app.config.from_object(Config)

CORS(
    app,
    resources={r"/api/*": {"origins": "http://localhost:3000"}},
    supports_credentials=True
)
db.init_app(app)
jwt = JWTManager(app)
app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(chat_bp, url_prefix='/api')
app.register_blueprint(message_bp, url_prefix='/api')
app.register_blueprint(upload_bp, url_prefix='/api')
with app.app_context():
        db.create_all()

if __name__ == '__main__':
        app.run(debug=True)