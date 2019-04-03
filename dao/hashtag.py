from dao.data import Data


class HashtagDAO:

    hashtags = Data().hashtags

    def getAllHashtags(self):
        return self.hashtags

    def getHashtagsByID(self, hID):
        hashtag = list(filter(lambda u: u['hashtag_id'] == hID, self.hashtags))
        return hashtag

    def getHashtagByPostId(self, pID):
        hashtag = list(filter(lambda u: u['post_id'] == pID, self.hashtags))
        return hashtag

    def getTrendingHashtag(self):
        hashtag = list(filter(lambda u: u['text'] == '#MINI', self.hashtags))
        return hashtag