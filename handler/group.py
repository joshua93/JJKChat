from flask import jsonify
from dao.group import GroupDAO

def mapGroupToDict(row):
    result = {}
    result['chat_group_id'] = row[0]
    result['chat_name'] = row[1]
    result['owner_id'] = row[2]
    return result

def mapUserToDict(row):
    result = {}
    result['user_id'] = row[0]
    result['first_name'] = row[1]
    result['last_name'] = row[2]
    result['email'] = row[3]
    result['phone'] = row[4]
    result['username'] = row[5]
    return result

class GroupHandler:
    # def getAllgroups(self):
    #     dao = GroupDAO()
    #     result = dao.getAllGroups()
    #     return jsonify(Users=result)

    def getAllGroups(self):
        dao = GroupDAO()
        result = dao.getAllGroups()
        mapped_result = []
        for r in result:
            mapped_result.append(mapGroupToDict(r))
        return jsonify(mapped_result)


    def createGroup(self, json):
        dao = GroupDAO()
        if len(json) != 2:
            return jsonify(Error="Malformed post request"), 400
        else:
            groupname = json['groupname']
            ownerId = json['ownerid']
            if groupname and ownerId:
                result = dao.createGroup(groupname, ownerId)
                return jsonify(result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteGroup(self, json):
        dao = GroupDAO()
        if len(json) != 2:
            return jsonify(Error="Malformed post request"), 400
        else:
            groupId = json['groupid']
            ownerId = json['ownerid']
            if groupId and ownerId:
                result = dao.deleteGroup(groupId, ownerId)
                return jsonify(result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def getGroupById(self, gID):
        dao = GroupDAO()
        result = dao.getGroupByID(gID)
        return jsonify(User=result)

    def getGroupOwnerByID(self, gID):
        dao = GroupDAO()
        result = dao.getGroupOwnerByID(gID)
        mapped_result = mapUserToDict(result)
        return jsonify(mapped_result)

    ##Edited by Jesi
    def getMembersByGroupID(self, gID):
        dao = GroupDAO()
        result = dao.getMembersByGroupID(gID)
        mapped_result = []
        for r in result:
            mapped_result.append(mapUserToDict(r))
        return jsonify(mapped_result)

    def addMember(self, gID, json):
        dao = GroupDAO()
        if len(json) != 1:
            return jsonify(Error="Malformed post request"), 400
        else:
            contactid = json['contactid']
            if contactid :
                result = dao.addContactTogroup(gID, contactid)
                return jsonify(result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def removeMember(self,gID,json):
        dao = GroupDAO()
        if len(json) != 1:
            return jsonify(Error="Malformed post request"), 400
        else:
            contactid = json['contactid']
            if contactid:
                result = dao.removeContactFromGroup(gID, contactid)
                return jsonify(result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def searchGroup(self,args):
        groupname = args.get("groupname")
        dao = GroupDAO()
        if groupname:
            result = dao.getGroupByName(groupname)
        return jsonify(result)