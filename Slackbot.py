from slacker import Slacker
from datetime import datetime

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

def BuildThreadIdList(messageIdList):
    threadList = []
    for msgId in messageIdList:
        if IsThread(generalChannelId, msgId):
            threadList.append(msgId)

    return threadList

def GetFirstAndLastMessageInThread(channelId, threadId):
    response = slack.conversations.replies(channelId, threadId)
    messageList = response.body["messages"]
    timeStampList = []
    for message in messageList:
        timeStampList.append(float(message["ts"]))

    first = min(float(timeStamp) for timeStamp in timeStampList)
    last = max(float(timeStamp) for timeStamp in timeStampList)

    return first, last


slack = Slacker('xoxb-1046012676599-1057769372852-jRVIxhLHfavSyzPODg669tvR')

generalChannelId = GetChannelId("general")
messageList = GetChannelHistory(generalChannelId)
messageIdList = GetMessageIdList(messageList)

threadIdList = BuildThreadIdList(messageIdList)

print(threadIdList)

for threadId in threadIdList:
    first, last = GetFirstAndLastMessageInThread(generalChannelId, threadId)
    conversationLength = round(((last - first) / 60), 2)
    print("Conversation began: " + str(datetime.fromtimestamp(first)) + " and ended: " + str(datetime.fromtimestamp(last)))
    print("The conversation was " + str(conversationLength) + " minutes long \n")


