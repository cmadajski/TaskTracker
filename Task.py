from datetime import date


class Task:

    name: str
    date: str
    status: bool
    rank: int

    def __init__(self, inName, inRank):
        self.name = inName
        today = date.today()
        self.date = today.strftime('%m/%d/%Y')
        self.status = False
        self.rank = inRank

    def updateStatus(self, inStatus: bool):
        self.status = inStatus

    def printTask(self):
        if not self.status:
            print(str(self.rank) + '. [ ] ' + self.name)
        else:
            print(str(self.rank) + '. [x] ' + self.name)
