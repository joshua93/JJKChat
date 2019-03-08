from dao.data import Data
import psycopg2

class GroupDAO:
    def __init__(self):
        DATABASE_URL = 'postgres://postgres:databaseclass@localhost:5432/jjkchat'
        self.conn = psycopg2._connect(DATABASE_URL)

    groups = Data().groups
    members = Data().group_members

    # def getAllGroups(self):
    #     return self.groups
    def getAllGroups(self):
        cursor = self.conn.cursor()
        query = "select * from chat_groups"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getGroupByID(self, gID):
        group = list(filter(lambda u: u['chat_group_id'] == gID, self.groups))
        return group

    def getGroupOwnerByID(self,gID):
        owner = list(filter(lambda u: u['chat_group_id'] == gID, self.groups))
        return owner

    def getMembersByGroupID(self,gID):
        members = list(filter(lambda u: u['chat_group_id'] == gID, self.members))
        return members

    def createGroup(self,groupname, ownerId):
        gID = "Group " + groupname + " created " + ownerId
        return gID

    def deleteGroup(self,groupname, ownerId):
        gID = "Group " + groupname + " deleted " + ownerId
        return gID

    def getGroupByName(self,gName):
        members = list(filter(lambda u: u['chat_group_name'] == gName, self.groups))
        return members

    def addContactTogroup(self,gId,uID):
        return "Contact added to group"

    def removeContactFromGroup(self,gId,uID):
        return "Contact removed from group"




