from dao.data import Data
import psycopg2
from config.dbconfig import pg_config


class PostDAO:
    def __init__(self):
        #DATABASE_URL = 'postgres://postgres:databaseclass@localhost:5432/jjkchat'
        DATABASE_URL = "dbname=%s user=%s password=%s host=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'], pg_config['host'])
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

    #Depracated use getNumberOfLikesForGivenPost instead
    def getLikesByPostId(self, pID):
        #cursor = self.conn.cursor()
        #query = "select count(*) from post natural inner join reactions where post_id=%s and reaction='like'"
        #cursor.execute(query,(pID,))
        return None

    def getNumberOfPostPerDay(self):
        return len(self.posts)

    def getNumberOfRepliesPerDay(self):
        return len(self.posts) #Just for demonstration

    def getNumberOfLikesPerDay(self):
        return 25 #Just for demonstration

    def getNumberOfDislikesPerDay(self):
        return 15 #Just for demonstration


    def getNumberOfLikesForGivenPost(self, pID):
        cursor = self.conn.cursor()
        query = "select count(*) from post natural inner join reactions where post_id=%s and reaction='like'"
        likes = cursor.execute(query,(pID,))
        
        return likes 

    def getNumberOfDislikesForGivenPost(self, pID):
        return 13 #Just for demonstration

    def getNumberOfRepliesForGivenPost(self, pID):
        return 34 #Just for demonstration

    def addPost(self, gID, aID, message,media):
        return "Message posted id 5"

    def getPostsPerDayByUser(self, uID):
        return len(self.posts) #Just for demonstration
 


