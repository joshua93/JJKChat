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

    def getOwnedGroupByUserID(self, uID):
        dao = UserDAO()
        result = dao.getOwnedGroupByUserID(uID)
        return jsonify(Groups=result)

    def getContactsbyUserID(self,uID):
        dao = UserDAO(x)
        result = dao.getContactsByUserID(uID)
        return jsonify(Contacts = result)


    def getMemberOfGroupsByUserID(self,uID):
        dao = UserDAO()
        result = dao.getMemberOfGroupsByUserID(uID)
        return jsonify(result)

