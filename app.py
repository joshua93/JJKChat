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
@app.route('/JJKChat/users/<int:uID>/contacts', methods=['GET','POST'])
def getContactsByUserID(uID):
    if request.method == 'POST':
        return UserHandler().addContactToContactList(uID,request.json)
    return UserHandler().getContactsbyUserID(uID)

#Gets to what groups a users is member of
@app.route('/JJKChat/users/<int:uID>/member', methods=['GET'])
def getMemberOfGroupsByUserID(uID):
    return UserHandler().getMemberOfGroupsByUserID(uID)


#Get all groups
@app.route('/JJKChat/groups', methods=['GET','POST'])
def getGroup():
    if request.method == 'POST':
        return GroupHandler().createGroup()
    if request.method == 'GET':
        return GroupHandler().getAllgroups()


#Get specific group by ID
@app.route('/JJKChat/groups/<int:gID>', methods=['GET'])
def getGroupByID(gID):
    return GroupHandler().getGroupById(gID)

#Gets specific groups owner by group ID
@app.route('/JJKChat/groups/<int:gID>/owner', methods=['GET'])
def getOwnerByGroupID(gID):
    return GroupHandler().getGroupOwnerByID(gID)

#Gets members of a group by group ID
@app.route('/JJKChat/groups/<int:gID>/members', methods=['GET'])
def getMembersByGroupID(gID):
    return GroupHandler().getMembersByGroupID(gID)

@app.route('/ChatApp/group/<int:gID>/member/<int:pID>', methods=['POST'])
def addMemberToGroup(gID, pID):
    return GroupHandler().addMember(gID, pID)

#Get all posts
@app.route('/JJKChat/posts', methods=['GET'])
def getAllPost():
    return PostHandler().getAllPost()

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
