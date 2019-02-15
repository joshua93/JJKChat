from dao.data import Data


class GroupDAO:

    groups = Data().groups
    members = Data().group_members

    def getAllGroups(self):
        return self.groups

    def getGroupByID(self, gID):
        group = list(filter(lambda u: u['chat_group_id'] == gID, self.groups))
        return group

    def getGroupOwnerByID(self,gID):
        owner = list(filter(lambda u: u['chat_group_id'] == gID, self.groups))
        return owner

    def getMembersByGroupID(self,gID):
        members = list(filter(lambda u: u['chat_group_id'] == gID, self.members))
        return members







