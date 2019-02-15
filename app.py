from flask import Flask
from handler.user import UserHandler
from handler.group import GroupHandler

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

@app.route('/JJKChat/users/<int:uID>/ownedgroups', methods=['GET'])
def getGroupByUserID(uID):
    return UserHandler().getGroupByUserID(uID)

@app.route('/JJKChat/users/<int:uID>/contacts', methods=['GET'])
def getContactsByUserID(uID):
    return UserHandler().getContactsbyUserID(uID)


@app.route('/JJKChat/groups', methods=['GET'])
def getGroup():
    return GroupHandler().getAllgroups()

@app.route('/JJKChat/groups/<int:gID>', methods=['GET'])
def getGroupByID(gID):
    return GroupHandler().getGroupById(gID)

@app.route('/JJKChat/groups/<int:gID>/owner', methods=['GET'])
def getOwnerByGroupID(gID):
    return GroupHandler().getGroupOwnerByID(gID)

@app.route('/JJKChat/groups/<int:gID>/members', methods=['GET'])
def getMembersByGroupID(gID):
    return GroupHandler().getMembersByGroupID(gID)

if __name__ == '__main__':
    app.run()
