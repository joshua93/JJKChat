from dao.data import Data


class UserDAO:

    users = Data().users
    groups = Data().groups
    contacts = Data().contacts
    posts = Data().posts
    members = Data().group_members

    def getAllUsers(self):
        return Data().users

    def loginUser(self, username, password):
        login = "Login Succesfull using " + username + " and " + password
        return login

    def getUserByID(self, uID):
        user = list(filter(lambda u: u['user_id'] == uID, self.users))
        return user

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

    def getContactsByUserID(self,uID):
        contacts = list(filter(lambda u: u['user_id'] == uID, self.contacts))
        return contacts

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


