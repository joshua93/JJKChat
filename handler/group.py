from flask import jsonify
from dao.group import GroupDAO


class GroupHandler:
    def getAllgroups(self):
        dao = GroupDAO()
        result = dao.getAllGroups()
        return jsonify(Users=result)

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
            groupId = json['groupId']
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
        return jsonify(Owner= result)

    def getMembersByGroupID(self, gID):
        dao = GroupDAO()
        result = dao.getMembersByGroupID(gID)
        return jsonify(Members= result)

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