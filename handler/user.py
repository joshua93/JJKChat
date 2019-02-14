from flask import jsonify
from dao.user import UserDAO


class UserHandler:
    def getAllUsers(self):
        dao = UserDAO()
        result = dao.getAllUsers()
        return jsonify(Users=result)

    def getUserById(self, uID):
        dao = UserDAO()
        result = dao.getUserByID(uID)
        return jsonify(User=result)

    def getGroupByUserID(self,uID):
        dao = UserDAO()
        result = dao.getGroupByUserID(uID)
        return jsonify(Groups=result)

    def getContactsbyUserID(self,uID):
        dao = UserDAO()
        result = dao.getContactsByUserID(uID)
        return  jsonify(Contacts = result)

