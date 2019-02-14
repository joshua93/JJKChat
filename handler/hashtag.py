from flask import jsonify

class hashtag:
    def _init_(self):
        self.hashtags = [
            {"hashtag_id" : 1, "text" : "#borrachoPelao", "post_id" : 1, "hashtag_date" : "Feb14"}
        ]

    def getAllHashtags(self):
        return jsonify(Hashtags=self.hashtags)

    def getHashtagById(self, hID):
        return jsonify(Hashtags=self.hashtags)

    def getHashtagByPostId(self, pID):
        return jsonify(Hashtags=self.hashtags)

    def getHashtagsByDate(self, date):
        return jsonify(Hashtags=self.hashtags) 

