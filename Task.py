from datetime import date


class Task:

    name: str
    date: str
    status: bool

    def __init__(self, inName):
        self.name = inName
        today = date.today()
        self.date = today.strftime('%m/%d/%Y')
        self.status = False

    def printTask(self):
        if not self.status:
            print('[ ] ' + self.name)
        else:
            print('[x] ' + self.name)