from slacker import Slacker
from datetime import datetime

global slack

def IsThread(channelId, messageId):
    response = slack.conversations.replies(channelId, messageId)

    return len(response.body["messages"]) > 1

def GetChannelId(channelName):
    response = slack.conversations.list()
    channelList = response.body["channels"]

    return next(channel["id"] for channel in channelList if channel["name"] == channelName)

def GetChannelHistory(channelId):
    response = slack.conversations.history(channelId)

    return response.body["messages"]

def GetMessageIdList(messageList):
    
    return [message["ts"] for message in messageList]

def BuildThreadIdList(messageIdList):

    return [msgId for msgId in messageIdList if IsThread(generalChannelId, msgId)]

def GetFirstAndLastMessageInThread(channelId, threadId):
    response = slack.conversations.replies(channelId, threadId)
    messageList = response.body["messages"]
    timeStampList = [message["ts"] for message in messageList]

    first = min(float(timeStamp) for timeStamp in timeStampList)
    last = max(float(timeStamp) for timeStamp in timeStampList)

    return first, last

def GetThreadMessageList(channelId, messageId):
    return slack.conversations.replies(channelId, messageId)
    
slack = Slacker('xoxb-1046012676599-1057769372852-KMbHWMFK1dXG36yxfOqUB1gX')

generalChannelId = GetChannelId("general")
messageList = GetChannelHistory(generalChannelId)
messageIdList = GetMessageIdList(messageList)

threadIdList = BuildThreadIdList(messageIdList)

for threadId in threadIdList:
    first, last = GetFirstAndLastMessageInThread(generalChannelId, threadId)
    conversationLength = round(((last - first) / 60), 2)
    print("Conversation began: " + str(datetime.fromtimestamp(first)) + " and ended: " + str(datetime.fromtimestamp(last)))
    print("The conversation was " + str(conversationLength) + " minutes long \n")


