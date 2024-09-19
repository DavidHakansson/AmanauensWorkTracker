from flask import Flask
from flask_login import LoginManager
from config import Config
from models import db, User
from routes import routes  
from auth import auth

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'  
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Create database tables
with app.app_context():
    db.create_all()

# Register blueprints
app.register_blueprint(auth)
app.register_blueprint(routes)  

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
