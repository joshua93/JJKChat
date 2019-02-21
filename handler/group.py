from flask import jsonify
from dao.group import GroupDAO


class GroupHandler:
    def getAllgroups(self):
        dao = GroupDAO()
        result = dao.getAllGroups()
        return jsonify(Users=result)

    def createGroup(self):
        return jsonify("Group Created")


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
        return  jsonify(Members= result)