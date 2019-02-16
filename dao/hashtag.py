class HashtagDAO:

    def __init__(self):
        self.hashtags = [
            {"hashtag_id": 1, "text": "#borrachoPelao", "post_id": 1, "hashtag_date": "02/14/2019"}
        ]

    def getAllHashtags(self):
        return self.users

    def getHashtagsByID(self, hID):
        hashtag = list(filter(lambda u: u['hashtag_id'] == hID, self.hashtags))
        return hashtag

    def getHashtagByPostId(self, pID):
        hashtag = list(filter(lambda u: u['post_id'] == pID, self.hashtags))
        return hashtag


    #Este metodo devuelve un entero (count)
    def getHashtagCount(self, text):
        hashtagList = list(filter(lambda u: u['post_id'] == pID, self.hashtags))
        return hashtagList






#

#With @inspectorG4dget's answer, if you want no duplicates, you can use set comprehensions instead of list comprehensions.

#>>> tags="Hey guys! #stackoverflow really #rocks #rocks #announcement"
#>>> {tag.strip("#") for tag in tags.split() if tag.startswith("#")}
#set(['announcement', 'rocks', 'stackoverflow'])
#Note that { } syntax for set comprehensions only works starting with Python 2.7.
#If you're working with older versions, feed list comprehension ([ ]) output to set function as suggested by @Bertrand.