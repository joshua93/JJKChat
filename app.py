from flask import Flask, request
from handler.user import UserHandler
from handler.group import GroupHandler
from handler.post import PostHandler
from handler.hashtag import HashtagHandler

app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome to JJKChat api"

@app.route('/JJKChat/login', methods=['POST'])
def loginUser():
    return UserHandler().loginUser(request.json)

#Get all users
@app.route('/JJKChat/users', methods=['GET','POST'])
def getAllUsers():
    if request.method == 'GET':
        if len(request.args) >= 1:
            return UserHandler().searchUser(request.args)
        else:
            return UserHandler().getAllUsers()
    if request.method == 'POST':
        return UserHandler().registerUser(request.json)


#Get specific user by ID
@app.route('/JJKChat/users/<int:uID>', methods=['GET'])
def getUserByID(uID):
    return UserHandler().getUserById(uID)


#get what groups th e user is owner of
@app.route('/JJKChat/users/<int:uID>/ownedgroups', methods=['GET'])
def getOwnedGroupByUserID(uID):
    return UserHandler().getOwnedGroupByUserID(uID)

#Gets contacts of a user
@app.route('/JJKChat/users/<int:uID>/contact', methods=['GET','POST','DELETE'])
def getContactsByUserID(uID):
    if request.method == 'POST':
        return UserHandler().addUserToContactList(uID, request.json)
    if request.method == 'GET':
        return UserHandler().getContactsbyUserID(uID)
    if request.method == 'DELETE':
        return UserHandler().removeContactsbyUserID(uID, request.json)

#Gets to what groups a users is member of
@app.route('/JJKChat/users/<int:uID>/member', methods=['GET'])
def getMemberOfGroupsByUserID(uID):
    return UserHandler().getMemberOfGroupsByUserID(uID)


#Get all groups
@app.route('/JJKChat/groups', methods=['GET','POST','DELETE'])
def getGroup():
    if request.method == 'GET':
        return GroupHandler().getAllgroups()
    if request.method == 'POST':
        return GroupHandler().createGroup(request.json)
    if request.method == 'DELETE':
        return GroupHandler().deleteGroup(request.json)

#Get specific group by ID
@app.route('/JJKChat/groups/<int:gID>', methods=['GET'])
def getGroupByID(gID):
    return GroupHandler().getGroupById(gID)

#Gets specific groups owner by group ID
@app.route('/JJKChat/groups/<int:gID>/owner', methods=['GET'])
def getOwnerByGroupID(gID):
    return GroupHandler().getGroupOwnerByID(gID)

#Gets members of a group by group ID
@app.route('/JJKChat/groups/<int:gID>/member', methods=['POST', 'GET','REMOVE'])
def getMembersByGroupID(gID):
    if request.method == 'GET':
        return GroupHandler().getMembersByGroupID(gID)
    if request.method == 'POST':
        return GroupHandler().addMember(gID, request.json)
    if request.method == 'POST':
        return GroupHandler().removeMember(gID, request.json)


#Get all posts
@app.route('/JJKChat/posts', methods=['GET','POST'])
def getAllPost():
    if request.method == 'GET':
        return PostHandler().getAllPost()
    elif request.method == 'POST':
        return PostHandler().addPost(request.json)


#Get specific post by Id
@app.route('/JJKChat/posts/<int:pID>', methods=['GET'])
def getPostByID(pID):
    return PostHandler().getPostByID(pID)

#Get specific user posts by user id
@app.route('/JJKChat/user/<int:uID>/post', methods=['GET'])
def getPostsByUserID(uID):
    return PostHandler().getPostsByUserID(uID)

#Get post by group id
@app.route('/JJKChat/group/<int:gID>/post', methods=['GET'])
def getPostByGroupId(gID):
    return PostHandler().getPostByGroupId(gID)

#Get the trending topic via hashtags
@app.route('/JJKChat/hashtag/top', methods=['GET'])
def getTrendingTopic():
    return HashtagHandler().getTrendingHashtag()

@app.route('/JJKChat/post/count', methods=['GET'])
def getNumberOfPostPerDay():
    return PostHandler().getNumberOfPostPerDay()

@app.route('/JJKChat/replies/count', methods=['GET'])
def getNumberOfRepliesPerDay():
    return PostHandler().getNumberOfRepliesPerDay()

@app.route('/JJKChat/likes/count', methods=['GET'])
def getNumberOfLikesPerDay():
    return PostHandler().getNumberOfLikesPerDay()

@app.route('/JJKChat/dislikes/count', methods=['GET'])
def getNumberOfDislikesPerDay():
    return PostHandler().getNumberOfDislikesPerDay()




if __name__ == '__main__':
    app.run()
