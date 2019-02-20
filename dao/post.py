from dao.data import Data


class PostDAO:
    posts = Data().posts

    def getAllPost(self):
        return self.posts

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
        posts = list(filter(lambda u: u['chat_group_id'] == gID, self.posts))
        return posts

    def getLikesByPostId(self, pID):
        likes = list(filter(lambda u: u['post_id'] == pID, self.posts))
        return likes

    def getNumberOfPostPerDY(self):
        return len(posts)






