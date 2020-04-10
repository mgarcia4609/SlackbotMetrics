from slacker import Slacker

class Channel:
    ID = 0
    Name = ''
    NumberOfUsers = []
    __channelList = []

    def __init__(self, slackConversationsListObject, channelName):
        self.__channelList = slackConversationsListObject.body["channels"]
        self.Name = channelName
        self.ID = self.__setChannelID()
        self.NumberOfUsers = self.__setNumberOfUsers()

    def __setChannelID(self):
        return next(channel["id"] for channel in self.__channelList if channel["name"] == self.Name)

    def __setNumberOfUsers(self):
        return next(channel["num_members"] for channel in self.__channelList if channel["name"] == self.Name)