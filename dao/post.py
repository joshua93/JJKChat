from dao.data import Data
import psycopg2
from config.dbconfig import pg_config


class PostDAO:

    def __init__(self):
        #DATABASE_URL = 'postgres://postgres:databaseclass@localhost:5432/jjkchat'
        DATABASE_URL = "dbname=%s user=%s password=%s host=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'], pg_config['host'])
        self.conn = psycopg2._connect(DATABASE_URL)

    posts = Data().posts

    def getAllPosts(self):
        cursor = self.conn.cursor()
        query = "select * from post"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPostsByGroupID(self, gID):
        cursor = self.conn.cursor()
        #query = "select * from post where chat_group_id = %s"

        query = """WITH plikes AS (SELECT post_id, count(*) AS likes
	                    FROM reactions
	                    WHERE reaction = 'like'
	                    GROUP BY post_id),
                    pdislikes AS (SELECT post_id, count(*) AS dislikes
	                    FROM reactions
	                    WHERE reaction = 'dislike'
	                    GROUP BY post_id)
                SELECT post.post_id, post.media, post.message, post.post_date, post.chat_group_id, post.user_id,likes, dislikes, users.username, users.first_name, users.last_name 
                FROM post natural inner join users LEFT JOIN plikes on post.post_id = plikes.post_id LEFT JOIN pdislikes on post.post_id = pdislikes.post_id
                WHERE post.chat_group_id =%s;"""
        cursor.execute(query,(gID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getNumberOfReactionsForGivenPost(self, pID, reaction):
        cursor = self.conn.cursor()
        query = "SELECT post_id, count(*) as likes FROM reactions  where post_id = %s and reaction =%s GROUP BY post_id"
        cursor.execute(query, (pID, reaction, ))
        likes = cursor.fetchone()
        return likes

    def getListOfUsersWhoReactedPost(self, pID, reaction):
        cursor = self.conn.cursor()
        query = "SELECT  user_id, first_name, last_name, username, reaction_date FROM reactions NATURAL INNER JOIN users WHERE post_id = %s AND reaction = %s"
        cursor.execute(query, (pID, reaction, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getNumberOfPostPerDay(self):
        cursor = self.conn.cursor()
        query = "SELECT post_date AS day, count(*) AS total FROM post GROUP BY post_date"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRepliesByPostID(self, pID):
        cursor = self.conn.cursor()
        query = "SELECT reply_id, reply_date, reply_message, post_id, user_id FROM reply WHERE post_id = %s"
        cursor.execute(query,(pID, ))
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

    def getNumberOfRepliesPerDay(self):
        return len(self.posts) #Just for demonstration

    def getNumberOfLikesPerDay(self):
        return 25 #Just for demonstration

    def getNumberOfDislikesPerDay(self):
        return 15 #Just for demonstration

    def getNumberOfRepliesForGivenPost(self, pID):
        return 34 #Just for demonstration

    def addPost(self, gID, aID, message,media):
        return "Message posted id 5"

    def getPostsPerDayByUser(self, uID):
        return len(self.posts) #Just for demonstration

