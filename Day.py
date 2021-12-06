from datetime import date
from Task import Task


class Day:

    tasks: list[Task]
    date: str
    tasksComplete: int

    def __init__(self):
        self.tasks = []
        today = date.today()
        self.date = today.strftime('%m/%d/%Y')
        self.tasksComplete = 0

    def addTask(self, inTask: Task):
        self.tasks.append(inTask)
        if inTask.status is True:
            self.tasksComplete += 1

    def updateTasksComplete(self, taskStatus: bool):
        if taskStatus is True:
            self.tasksComplete += 1
        else:
            self.tasksComplete -= 1