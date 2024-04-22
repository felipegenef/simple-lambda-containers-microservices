from flask import Flask, Blueprint

app = Flask(__name__)
api = Blueprint('app', __name__, url_prefix="/py/api")

@api.get("")
def hello():
    return "Hello from Python Microservice!"

if __name__ == "__main__":
    app.register_blueprint(api)
    app.run(port=8080)