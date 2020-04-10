from slacker import Slacker

class Message:
    TimeStamp = 0.0
    ParentTimeStamp = 0.0
    UserId = ""
    UserName = ""

    def __init__(self, message):

        self.Timestamp = message.Timestamp
        self.ParentTimeStamp = message.ParentTimeStamp
        self.UserId = message.UserId
        self.UserName = message.UserName
