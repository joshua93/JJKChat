from flask import jsonify
from dao.post import PostDAO


class PostHandler:
    def getAllPost(self):
        dao = PostDAO()
        result = dao.getAllPost()
        return jsonify(Posts=result)

    def getPostByID(self, pID):
        dao = PostDAO()
        result = dao.getPostByID(pID)
        return jsonify(Post=result)

    def getMessageByPostID(self, pID):
        dao = PostDAO()
        result = dao.getMessageByPostID(pID)
        return jsonify(Message=result)

    def getMediaByPostID(self,pID):
        dao = PostDAO()
        result = dao.getMediaByPostID(pID)
        return jsonify(Contacts = result)

    def getAuthorByPostID(self,pID):
        dao = PostDAO()
        result = dao.getAuthorByPostID(pID)
        return jsonify(Author = result)

    def getPostsByUserID(self,uID):
        dao = PostDAO()
        result = dao.getPostsByUserID(uID)
        return jsonify(Post = result)

    def getPostByGroupId(self,gID):
        dao = PostDAO()
        result = dao.getPostByGroupId(gID)
        return jsonify(Post = result)

    def getLikesByPostId(self,pID):
        dao = PostDAO()
        result = dao.getLikesByPostId(pID)
        return jsonify(Likes = result)

    def getNumberOfPostPerDay(self):
        dao = PostDAO()
        result = dao.getNumberOfPostPerDay()
        return jsonify(Posts = result)

    def getNumberOfRepliesPerDay(self):
        dao = PostDAO()
        result = dao.getNumberOfRepliesPerDay()
        return jsonify(Replies = result)

    def getNumberOfLikesPerDay(self):
        dao = PostDAO()
        result = dao.getNumberOfLikesPerDay()
        return jsonify(Likes = result)
