from flask import Flask
from handler.user import UserHandler

app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome to JJKChat api"


@app.route('/JJKChat/users', methods=['GET'])
def getUsers():
    return UserHandler().getAllUsers()

@app.route('/JJKChat/users/<int:uID>', methods=['GET'])
def getUserByID(uID):
    return UserHandler().getUserById(uID)


if __name__ == '__main__':
    app.run()
