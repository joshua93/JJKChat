from flask import Flask, request
from handler.user import UserHandler
from handler.group import GroupHandler
from handler.post import PostHandler
from handler.hashtag import HashtagHandler
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
CORS(app)

@app.route('/')
def home():
    return "Welcome to JJKChat api"

# Operation 2 Login an existing user
@app.route('/JJKChat/login', methods=['POST'])
def loginUser():
    return UserHandler().loginUser(request.json)

# Operation 1; Get all users #Search for a user #Register a user
@app.route('/JJKChat/users', methods=['GET','POST'])
def getAllUsers():
    if request.method == 'GET':
        if len(request.args) >= 1:
            return UserHandler().searchUser(request.args)
        else:
            return UserHandler().getAllUsers()
    if request.method == 'POST':
        return UserHandler().registerUser(request.json)

# Operation 3, 8 Get all groups Create a chatgroup Delete a Chatgroup
@app.route('/JJKChat/groups', methods=['GET','POST','DELETE'])
def getGroup():
    if request.method == 'GET':
        return GroupHandler().getAllGroups()
    if request.method == 'POST':
        return GroupHandler().createGroup(request.json)
    if request.method == 'DELETE':
        return GroupHandler().deleteGroup(request.json)


# Operation 4, 7 Gets contacts of an user . Add user to contacts
@app.route('/JJKChat/users/<int:uID>/contact', methods=['GET','POST','DELETE'])
def getContactsByUserID(uID):
    if request.method == 'POST':
        return UserHandler().addUserToContactList(uID, request.json)
    if request.method == 'GET':
        return UserHandler().getContactsbyUserID(uID)
    if request.method == 'DELETE':
        return UserHandler().removeContactsbyUserID(uID, request.json)

# Operation 5, 6 Gets members of a group by group ID
# Implemented GET
@app.route('/JJKChat/group/<int:gID>/member', methods=['POST', 'GET','DELETE'])
def getMembersByGroupID(gID):
    if request.method == 'GET':
        return GroupHandler().getMembersByGroupID(gID)
    if request.method == 'POST':
        return GroupHandler().addMember(gID, request.json)
    if request.method == 'DELETE':
        return GroupHandler().removeMember(gID, request.json)

# Operation 9, 10, 13 Get post by group id
@app.route('/JJKChat/group/<int:gID>/post', methods=['GET','POST'])
def getPostByGroupId(gID):
    if request.method == 'GET':
        return PostHandler().getPostByGroupId(gID)
    elif request.method == 'POST':
        return PostHandler().addPost(gID,request.json)

@app.route('/JJKChat/group/<int:gID>/post/react', methods=['GET','POST'])
def reactToaPost(gID):
    if request.method == 'GET':
        return PostHandler().getReaction(request.json)
    elif request.method == 'POST':
        return PostHandler().react(gID,request.json)


#Get specific user by ID
@app.route('/JJKChat/users/<int:uID>', methods=['GET'])
def getUserByID(uID):
    return UserHandler().getUserById(uID)


#get what groups th e user is owner of
@app.route('/JJKChat/users/<int:uID>/ownedgroups', methods=['GET'])
def getOwnedGroupByUserID(uID):
    return UserHandler().getOwnedGroupByUserID(uID)



#Gets to what groups a users is member of
@app.route('/JJKChat/users/<int:uID>/member', methods=['GET'])
def getMemberOfGroupsByUserID(uID):
    return UserHandler().getMemberOfGroupsByUserID(uID)



#Get specific group by ID
@app.route('/JJKChat/groups/<int:gID>', methods=['GET'])
def getGroupByID(gID):
    return GroupHandler().getGroupById(gID)

#Gets specific groups owner by group ID
@app.route('/JJKChat/groups/<int:gID>/owner', methods=['GET'])
def getOwnerByGroupID(gID):
    return GroupHandler().getGroupOwnerByID(gID)



#Get all posts
@app.route('/JJKChat/posts', methods=['GET','POST'])
def getAllPost():
    if request.method == 'GET':
        return PostHandler().getAllPost()



#Get specific post by Id
@app.route('/JJKChat/posts/<int:pID>', methods=['GET'])
def getPostByID(pID):
    return PostHandler().getPostByID(pID)

#Get specific user posts by user id
@app.route('/JJKChat/user/<int:uID>/post', methods=['GET'])
def getPostsByUserID(uID):
    return PostHandler().getPostsByUserID(uID)

# #Get post by group id
# @app.route('/JJKChat/group/<int:gID>/post', methods=['GET'])
# def getPostByGroupId(gID):
#     return PostHandler().getPostByGroupId(gID)

# Statistics 1; Get the trending topic via hashtags
@app.route('/JJKChat/hashtag/top', methods=['GET'])
def getTrendingTopic():
    return HashtagHandler().getTrendingHashtag()

# Statistics 2 Get total number of posts on a certain date
@app.route('/JJKChat/user/<int:uID>/post/count', methods=['GET'])
def getNumberOfPostPerDayByUser(uID):
    return PostHandler().getNumberOfPostPerDayByUser(uID)

# Statistics 3
@app.route('/JJKChat/replies/count', methods=['GET'])
def getNumberOfRepliesPerDay():
    return PostHandler().getNumberOfRepliesPerDay()

# Statistics 4
@app.route('/JJKChat/likes/count', methods=['GET'])
def getNumberOfLikesPerDay():
    return PostHandler().getNumberOfLikesPerDay()

#statistics 5
@app.route('/JJKChat/dislikes/count', methods=['GET'])
def getNumberOfDislikesPerDay():
    return PostHandler().getNumberOfDislikesPerDay()

#Statistics 9
#********************METODO TEMPORERO. LA IDEA ES PASARLE EL REACTION COMO PARAMETRO*****************
@app.route('/JJKChat/likes/<int:pID>/count', methods=['GET'])
def getNumberOfLikesForGivenPost(pID):
    return PostHandler().getNumberOfLikesForGivenPost(pID)

@app.route('/JJKChat/dislikes/<int:pID>/count', methods=['GET'])
def getNumberOfDislikesForGivenPost(pID):
    return PostHandler().getNumberOfDislikesForGivenPost(pID)

#Statistics 8
@app.route('/JJKChat/replies/<int:pID>/count', methods=['GET'])
def getNumberOfRepliesForGivenPost(pID):
    return PostHandler().getNumberOfRepliesForGivenPost(pID)

#Statistics 7 Get specific user posts number by user id
@app.route('/JJKChat/user/<int:uID>/post/today', methods=['GET'])
def getPostsPerDayByUser(uID):
    return PostHandler().getPostsPerDayByUser(uID)

@app.route('/JJKChat/user/mostactive', methods=['GET'])
def getMostActiveUser():
    return UserHandler().getMostActiveUser()

#********************METODO TEMPORERO. LA IDEA ES PASARLE EL REACTION COMO PARAMETRO*****************
@app.route('/JJKChat/post/<int:pID>/likes', methods=['GET'])
def getListOfUsersWhoLikedPost(pID):
    return PostHandler().getListOfUsersWhoLikedPost(pID)

@app.route('/JJKChat/post/<int:pID>/dislikes', methods=['GET'])
def getListOfUsersWhoDislikedPost(pID):
    return PostHandler().getListOfUsersWhoDislikedPost(pID)



if __name__ == '__main__':
    app.run()
