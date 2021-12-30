from Day import Day

class User:

    days: list[Day] = []
    name: str
    email: str
    numDays: int = 0
    tasksTotal: int = 0
    completedTotal: int = 0
    daysTotal: int = 0

    def __init__(self, inputName: str, inputEmail: str):
        self.name = inputName
        self.email = inputEmail
        self.numDays = 0
        self.numTasks = 0

    def addDay(self, newDay: Day):
        self.numDays += 1
