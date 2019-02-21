from flask import jsonify
from dao.user import UserDAO


class UserHandler:
    def getAllUsers(self):
        dao = UserDAO()
        result = dao.getAllUsers()
        return jsonify(Users=result)

    def loginUser(self):
       # print(json)
        dao = UserDAO()
       # username = json['username']
        #password = json['password']
       # result = dao.loginUser(username,password)
        return jsonify("Login")

    def getUserById(self, uID):
        dao = UserDAO()
        result = dao.getUserByID(uID)
        return jsonify(User=result)

    def getOwnedGroupByUserID(self, uID):
        dao = UserDAO()
        result = dao.getOwnedGroupByUserID(uID)
        return jsonify(Groups=result)

    def getContactsbyUserID(self,uID):
        dao = UserDAO()
        result = dao.getContactsByUserID(uID)
        return jsonify(Contacts = result)

    def getMemberOfGroupsByUserID(self,uID):
        dao = UserDAO()
        result = dao.getMemberOfGroupsByUserID(uID)
        return jsonify(result)


    def searchUser(self, args):
        first_name = args.get("first_name")
        email = args.get("email")
        phone = args.get("phone")
        dao = UserDAO()
        if email:
            result = dao.getUserByEmail(email)
        elif phone:
            result = dao.getUserByPhone(phone)
        elif first_name:
            result = dao.getUserByFirstName(first_name)
        return jsonify(result)