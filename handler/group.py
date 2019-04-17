from flask import jsonify
from dao.group import GroupDAO
from dictionaryMapping import *


class GroupHandler:

    def getAllGroups(self):
        dao = GroupDAO()
        result = dao.getAllGroups()
        if not result:
            return jsonify(Error="Not found"), 404
        mapped_result = []
        for r in result:
            mapped_result.append(mapGroupToDict(r))
        return jsonify(mapped_result)

    def getGroupOwnerByGroupID(self, gID):
        dao = GroupDAO()
        result = dao.getGroupOwnerByGroupID(gID)
        if not result:
            return jsonify(Error="Not found"), 404
        mapped_result = mapUserToDict(result)
        return jsonify(mapped_result)

    def getGroupMembersByGroupID(self, gID):
        dao = GroupDAO()
        result = dao.getGroupMembersByGroupID(gID)
        if not result:
            return jsonify(Error="Not found"), 404
        mapped_result = []
        for r in result:
            mapped_result.append(mapUserToDict(r))
        return jsonify(mapped_result)

    def getGroupByGroupID(self, gID):
        dao = GroupDAO()
        result = dao.getGroupByGroupID(gID)
        if not result:
            return jsonify(Error="Not found"), 404
        mapped_result = mapGroupToDict(result)
        return jsonify(mapped_result)

    def createGroup(self, json):
        dao = GroupDAO()
        chat_name = json['chat_name']
        ownerId = json['user_id']
        result = dao.createGroup(chat_name, ownerId)
        return jsonify(result), 201


    def deleteGroup(self, json):
        dao = GroupDAO()
        chat_group_id = json['chat_group_id']
        ownerId = json['user_id']
        result = dao.deleteGroup(chat_group_id, ownerId)
        return jsonify(result), 201


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
            contactid = json['user_id']
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