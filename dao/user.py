from dao.data import Data
import psycopg2


class UserDAO:

    def __init__(self):
        DATABASE_URL = 'postgres://postgres:databaseclass@localhost:5432/jjkchat'
        self.conn = psycopg2._connect(DATABASE_URL)

    users = Data().users
    groups = Data().groups
    contacts = Data().contacts
    posts = Data().posts
    members = Data().group_members

    # def getAllUsers(self):
    #     return Data().users

    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = "select * from users;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result


    def loginUser(self, username, password):
        login = "Login Succesfull using " + username + " and " + password
        return login

    # def getUserByID(self, uID):
    #     user = list(filter(lambda u: u['user_id'] == uID, self.users))
    #     return user

    def getUserByID(self,uID):
        cursor = self.conn.cursor()
        query = "select * from users where user_id = %s;"
        cursor.execute(query,(uID,))
        result = cursor.fetchone()
        return result

    def getUserByFirstName(self,uFN):
        user = list(filter(lambda u: u['first_name'] == uFN, self.users))
        return user

    def getUserByLastName(self, uLN):
        user = list(filter(lambda u: u['last_name'] == uLN, self.users))
        return user

    def getUserByPhone(self, uPn):
        user = list(filter(lambda u: u['phone'] == uPn, self.users))
        return user

    def getUserByEmail(self, uEm):
        user = list(filter(lambda u: u['email'] == uEm, self.users))
        return user

    def getUserByUsername(self, uUn):
        user = list(filter(lambda u: u['username'] == uUn, self.users))
        return user

    def getOwnedGroupByUserID(self, uID):
        group = list(filter(lambda u: u['owner_id'] == uID, self.groups))
        return group

    # def getContactsByUserID(self,uID):
    #     contacts = list(filter(lambda u: u['user_id'] == uID, self.contacts))
    #     return contacts

    def getContactsByUserID(self, uID):
        cursor = self.conn.cursor()
        query = "select * from contact INNER JOIN users on contact.contact_user_id = users.user_id where contact.user_id = %s;"
        cursor.execute(query,(uID,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getReplyByUserID(self,uID):
        posts = list(filter(lambda u: u['user_id'] == uID, self.users))
        return posts

    def getMemberOfGroupsByUserID(self,uID):
        memberof = list(filter(lambda u: u['user_id'] == uID, self.members))
        return memberof

    def registerUser(self,username, password, firstname, lastname, phone, email):
        return "5"

    def addContact(self,uID, firstname, lastname, phone, email):
        return "Done"

    def getMostActiveUser(self):
        return list(filter(lambda u: u['user_id'] == 2, self.contacts))  #Second user of Data table. Just for demonstration


