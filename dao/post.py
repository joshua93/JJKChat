from dao.data import Data
import psycopg2


class PostDAO:
    def __init__(self):
        DATABASE_URL = 'postgres://postgres:databaseclass@localhost:5432/jjkchat'
        self.conn = psycopg2._connect(DATABASE_URL)

    posts = Data().posts

    # def getAllPost(self):
    #     return self.posts

    def getAllPost(self):
        cursor = self.conn.cursor()
        query = "select * from post"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result



    def getPostByID(self, pID):
        post = list(filter(lambda u: u['post_id'] == pID, self.posts))
        return post

    def getMessageByPostID(self,pID):
        message = list(filter(lambda u: u['post_id'] == pID, self.posts))
        return message

    def getMediaByPostID(self, pID):
        media = list(filter(lambda u: u['post_id'] == pID, self.posts))
        return media

    def getAuthorByPostID(self, pID):
        user = list(filter(lambda u: u['post_id'] == pID, self.posts))
        return user

    def getPostsByUserID(self, uID):
        posts = list(filter(lambda u: u['post_author_id'] == uID, self.posts))
        return posts

    def getPostByGroupId(self, gID):
        cursor = self.conn.cursor()
        query = "select * from post where chat_group_id = %s"
        cursor.execute(query,(gID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getLikesByPostId(self, pID):
        likes = list(filter(lambda u: u['post_id'] == pID, self.posts))
        return likes

    def getNumberOfPostPerDay(self):
        return len(self.posts)

    def getNumberOfRepliesPerDay(self):
        return len(self.posts) #Just for demonstration

    def getNumberOfLikesPerDay(self):
        return 25 #Just for demonstration

    def getNumberOfDislikesPerDay(self):
        return 15 #Just for demonstration


    def getNumberOfLikesForGivenPost(self, pID):
        return 20 #Just for demonstration

    def getNumberOfDislikesForGivenPost(self, pID):
        return 13 #Just for demonstration

    def getNumberOfRepliesForGivenPost(self, pID):
        return 34 #Just for demonstration

    def addPost(self, gID, aID, message,media):
        return "Message posted id 5"

    def getPostsPerDayByUser(self, uID):
        return len(self.posts) #Just for demonstration
 


