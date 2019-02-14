class UserDAO:

    def __init__(self):
        self.users = [
            {"user_id": 1, "first_name": "Orrin", "last_name": "Palombi", "email": "opalombi0@spiegel.de","phone": "877-264-5336", "password": "mECoavG", "username": "opalombi0"},
            {"user_id": 2, "first_name": "Enrique", "last_name": "Scammell", "email": "escammell1@yellowbook.com","phone": "820-621-8379", "password": "YHLEmb", "username": "escammell1"},
            {"user_id": 3, "first_name": "Stephine", "last_name": "Arnley", "email": "sarnley2@drupal.org","phone": "261-778-8034", "password": "6R7eTgZ6", "username": "sarnley2"},
            {"user_id": 4, "first_name": "Olimpia", "last_name": "Itzik", "email": "oitzik3@yelp.com","phone": "870-457-3079", "password": "nmyVcchad8", "username": "oitzik3"},
            {"user_id": 5, "first_name": "Serge", "last_name": "Labat", "email": "slabat4@sina.com.cn","phone": "670-777-4902", "password": "ONXd7UJ", "username": "slabat4"},
            {"user_id": 6, "first_name": "Noam", "last_name": "Hand", "email": "nhand5@liveinternet.ru","phone": "220-172-7328", "password": "NmQ4U51DRLGk", "username": "nhand5"},
            {"user_id": 7, "first_name": "Merlina", "last_name": "Crisell", "email": "mcrisell6@usnews.com","phone": "844-715-3735", "password": "sw37sJ8pm", "username": "mcrisell6"},
            {"user_id": 8, "first_name": "Danna", "last_name": "Pawlaczyk", "email": "dpawlaczyk7@squidoo.com","phone": "573-216-8507", "password": "DyyhvZ", "username": "dpawlaczyk7"},
            {"user_id": 9, "first_name": "Moore", "last_name": "Iacovini", "email": "miacovini8@businesswire.com","phone": "538-338-0128", "password": "0eFnhk", "username": "miacovini8"},
            {"user_id": 10, "first_name": "Clarie", "last_name": "Fosken", "email": "cfosken9@ustream.tv","phone": "778-725-0847", "password": "PWDHZw40", "username": "cfosken9"}
        ]

    def getAllUsers(self):
        return self.users

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





