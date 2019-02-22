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
                gID = dao.createGroup(groupname, ownerId)
                result = "Group created id " + gID
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

    def addMember(self):
        return "Member Added to Group"

    def searchGroup(self,args):
        groupname = args.get("groupname")
        dao = GroupDAO()
        if groupname:
            result = dao.getGroupByName(groupname)
        return jsonify(result)