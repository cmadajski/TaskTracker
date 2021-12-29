from Day import Day

class User:

    days: list[Day] = []
    name: str
    email: str
    numDays: int
    numTasks: int
    tasksCompleted: int
    daysCompleted: int

    def __init__(self, inputName: str, inputEmail: str):
        self.name = inputName
        self.email = inputEmail