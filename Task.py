

class Task:

    name: str
    status: bool
    rank: int

    def __init__(self, inName, inRank):
        self.name = inName
        self.status = False
        self.rank = inRank

    def updateStatus(self, inStatus: bool):
        self.status = inStatus


    def printTask(self):
        if not self.status:
            print(str(self.rank) + '. [ ] ' + self.name)
        else:
            print(str(self.rank) + '. [x] ' + self.name)
