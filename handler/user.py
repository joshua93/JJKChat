from flask import  jsonify

class UserHandler:

    def getAllUsers(self):
        dao = UserDAO()
        result = dao.getallusers()
        mapped_result = []
        for r in result:
            mapped_result.append(self.map_to_dict(r))
        return jsonify(Part=mapped_result)


    def getUserById(self, uID):
        user = list(filter(lambda u: u['user_id'] == uID, self.users))
        return jsonify(Users=user)
