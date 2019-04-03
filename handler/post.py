from flask import jsonify
from dao.post import PostDAO
from dictionaryMapping import *


class PostHandler:

    def getAllPost(self):
        dao = PostDAO()
        result = dao.getAllPosts()
        mapped_result = []
        for r in result:
            mapped_result.append(mapPostToDict(r))
        return jsonify(mapped_result)

    def getPostByGroupId(self,gID):
        dao = PostDAO()
        result = dao.getPostsByGroupID(gID)
        mapped_result = []
        for r in result:
            mapped_result.append(mapPostToDict2(r))
        return jsonify(mapped_result)

    def getNumberOfLikesForGivenPost(self, pID):
        dao = PostDAO()
        result = dao.getNumberOfReactionsForGivenPost(pID, "like")
        mapped_result = mapReacCountToDict(result)
        return jsonify(mapped_result)

    def getNumberOfDislikesForGivenPost(self, pID):
        dao = PostDAO()
        result = dao.getNumberOfReactionsForGivenPost(pID, "dislike")
        mapped_result = mapReacCountToDict(result)
        return jsonify(mapped_result)

    def getListOfUsersWhoLikedPost(self, pID):
        dao = PostDAO()
        result = dao.getListOfUsersWhoReactedPost(pID, "like")
        mapped_result = []
        for r in result:
            mapped_result.append(mapToReactDict(r))
        return jsonify(mapped_result)

    def getListOfUsersWhoDislikedPost(self, pID):
        dao = PostDAO()
        result = dao.getListOfUsersWhoReactedPost(pID, "dislike")
        mapped_result = []
        for r in result:
            mapped_result.append(mapToReactDict(r))
        return jsonify(mapped_result)

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

    def getNumberOfDislikesPerDay(self):
        dao = PostDAO()
        result = dao.getNumberOfDislikesPerDay()
        return jsonify(Dislikes = result)

    def getNumberOfRepliesForGivenPost(self, pID):
        dao = PostDAO()
        result = dao.getNumberOfRepliesForGivenPost(pID)
        return jsonify(Replies = result)

    def addPost(self,gID, json):
        dao = PostDAO()
        if len(json) != 2:
            return jsonify(Error="Malformed post request"), 400
        else:
            groupID = json['groupID']
            author = json['author']
            message = json['message']
            media = json['media']

            if groupID and author and message and media:
                gID = dao.addPost(groupID, author,message, media)

                return jsonify(gID), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def getPostsPerDayByUser(self,uID):
        dao = PostDAO()
        result = dao.getPostsPerDayByUser(uID)
        return jsonify(Posts = result)

    def getNumberOfPostPerDayByUser(self, uID):
        dao = PostDAO()
        result = "5"
        return  jsonify(result)

    def react(self, gID, json):
        return "You reacted to this post"

    def getReaction(self, json):
        return"55 likes"
