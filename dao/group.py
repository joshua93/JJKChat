from dao.data import Data
import psycopg2
from config.dbconfig import pg_config


class GroupDAO:

    groups = Data().groups
    members = Data().group_members

    def __init__(self):
        #DATABASE_URL = 'postgres://postgres:databaseclass@localhost:5432/jjkchat'
        DATABASE_URL = "dbname=%s user=%s password=%s host=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'], pg_config['host'])
        self.conn = psycopg2._connect(DATABASE_URL)

    def getAllGroups(self):
        cursor = self.conn.cursor()
        query = "select * from chat_groups"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGroupOwnerByID(self,gID):
        cursor = self.conn.cursor()
        query = "select user_id, first_name, last_name , email, phone, username  from chat_groups natural inner JOIN users where chat_group_id = %s "
        cursor.execute(query, (gID,))
        result = cursor.fetchone()
        return result

    def getMembersByGroupID(self,gID):
        cursor = self.conn.cursor()
        query = "select user_id, first_name, last_name, email, phone,  username from chat_group_members natural inner join users where chat_group_id = %s"
        cursor.execute(query, (gID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGroupByID(self, gID):
        group = list(filter(lambda u: u['chat_group_id'] == gID, self.groups))
        return group

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