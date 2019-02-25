from flask import jsonify
from dao.user import UserDAO


class UserHandler:
    def getAllUsers(self):
        dao = UserDAO()
        result = dao.getAllUsers()
        return jsonify(Users=result)

    def loginUser(self, json):
        dao = UserDAO()
        if json is None:
            return jsonify(Error="Malformed post request"), 400

        username = json['username']
        password = json['password']

        if username and password:
            result = dao.loginUser(username,password)
            return jsonify(result)

        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def registerUser(self, json):
        dao = UserDAO()
        if len(json) != 6:
            return jsonify(Error="Malformed post request"), 400
        else:
            username = json['username']
            password = json['password']
            firstname = json['firstname']
            lastname = json['lastname']
            phone = json['phone']
            email = json['email']
            if username and password and firstname and lastname and phone and email:
                uID = dao.registerUser(username, password, firstname, lastname, phone, email)
                result = "User created with id " + uID
                return jsonify(result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

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

    def addUserToContactList(self, uID, json):
        dao = UserDAO()
        if len(json) != 4:
            return jsonify(Error="Malformed post request"), 400
        else:
            firstname = json['firstname']
            lastname = json['lastname']
            phone = json['phone']
            email = json['email']
            if firstname and lastname and phone:
                uID = dao.addContact(uID, firstname, lastname, phone, None)
                result = "User was added to contactlist"
                return jsonify(result), 201
            elif firstname and lastname and email:
                uID = dao.addContact(uID, firstname, lastname, None, email)
                result = "User was added to contactlist"
                return jsonify(result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def removeContactsbyUserID(self,uID,json):
        return "Contact removed"

    def searchUser(self, args):
        first_name = args.get("name")
        email = args.get("email")
        phone = args.get("phone")
        username = args.get("username")
        dao = UserDAO()
        if email:
            result = dao.getUserByEmail(email)
        elif phone:
            result = dao.getUserByPhone(phone)
        elif first_name:
            result = dao.getUserByFirstName(first_name)
        elif username:
            result =  dao.getUserByUsername(username)
        return jsonify(result)

    def getMostActiveUserByDate(self, date):
        dao = UserDAO()
        result = dao.getMostActiveUserByDate(date)
        return jsonify(result)