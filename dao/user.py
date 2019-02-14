from dao.data import Data


class UserDAO:

    users = Data().users
    posts = Data().posts

    def getAllUsers(self):
        return Data().users

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





