from datetime import timedelta
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api

from app.resources.transaction import TransactionList
from app.resources.user import UserRegister, UserLogin
from app.config.config import postgresqlConfig

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = postgresqlConfig
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["JWT_SECRET_KEY"] = "JWT123SACRETKEY"
app.config['JWT_TOKEN_LOCATION'] = ['headers']
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=10)

app.config.from_pyfile('config/config.py')

jwt = JWTManager(app)
api = Api(app, prefix="/api/v3")


@app.before_first_request
def create_tables():
    from app.config.db import db
    db.init_app(app)
    db.create_all()


api.add_resource(UserRegister, '/register', methods=['POST'])
api.add_resource(UserLogin, '/merchant/user/login', methods=['POST'])
api.add_resource(TransactionList, '/transactions/report', methods=['POST'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000',debug=True)