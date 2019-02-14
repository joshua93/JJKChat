class HashtagDAO:

    def __init__(self):
        self.hashtags = [
            {"hashtag_id": 1, "text": "#borrachoPelao", "post_id": 1, "hashtag_date": "Feb14"}
        ]

    def getAllHashtags(self):
        return self.users

    def getHashtagsByID(self, hID):
        hashtag = list(filter(lambda u: u['hashtag_id'] == hID, self.hashtags))
        return hashtag

    def getHashtagByPostId(self, pID):
        hashtag = list(filter(lambda u: u['post_id'] == pID, self.hashtags))
        return hashtag





