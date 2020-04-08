from slacker import Slacker

global slack

def IsThread(channelId, messageId):
    response = slack.conversations.replies(channelId, messageId)
    if len(response.body["messages"]) > 1:
        return True

def GetChannelId(channelName):
    response = slack.conversations.list()
    channelList = response.body["channels"]

    for channel in channelList:
        if channel["name"] == channelName:
            channelId = channel["id"]

    return channelId

def GetChannelHistory(channelId):
    response = slack.conversations.history(channelId)
    messageList = response.body["messages"]

    return messageList

def GetMessageIdList(messageList):
    messageIdList = []
    for message in messageList:
        messageIdList.append(message["ts"])
    
    return messageIdList

def BuildThreadList(messageIdList):
    threadList = []
    for msgId in messageIdList:
        if IsThread(generalChannelId, msgId):
            threadList.append(msgId)

    return threadList

slack = Slacker('xoxb-1046012676599-1057769372852-zQpZiCMqBiChot24ZOedzS5N')

generalChannelId = GetChannelId("general")
messageList = GetChannelHistory(generalChannelId)
messageIdList = GetMessageIdList(messageList)

print(messageIdList)

threadList = BuildThreadList(messageIdList)

print(threadList)


