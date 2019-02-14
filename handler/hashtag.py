from flask import jsonify
from dao.hashtag import HashtagDAO

class Hashtag:

    def getAllHashtags(self):
        dao = HashtagDAO()
        result = dao.getAllHashtags()
        return jsonify(result)

    def getHashtagById(self, hID):
        dao = HashtagDAO()
        result = dao.getHashtagsByID()
        return jsonify(result)

    def getHashtagByPostId(self, pID):
        dao = HashtagDAO()
        result = dao.getHashtagByPostId()
        return jsonify(result)

   # def getHashtagsByDate(self, date):
    #    return jsonify(Hashtags=self.hashtags)

