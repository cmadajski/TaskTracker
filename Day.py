from datetime import date
from Task import Task


class Day:

    tasks: list[Task]
    date: str
    tasksComplete: int
    numTasks: int

    def __init__(self):
        self.tasks = []
        today = date.today()
        self.date = today.strftime('%m/%d/%Y')
        self.tasksComplete = 0
        self.numTasks = 0

    def addTask(self, inTask: Task):
        self.tasks.append(inTask)
        if inTask.status is True:
            self.tasksComplete += 1
        self.numTasks += 1

    def removeTask(self, inputVal):
        # remove by index
        if type(inputVal) is int:
            self.numTasks -= 1
            if self.tasks[inputVal].status is True:
                self.tasksComplete -= 1
            self.tasks.pop(inputVal - 1)
        # remove by name
        elif type(inputVal) is str:
            # find the task in the list
            taskIndex = -1
            for x in self.tasks:
                if x.name == inputVal:
                    taskIndex = x.rank - 1
            self.numTasks -= 1
            if self.tasks[taskIndex].status is True:
                self.tasksComplete -= 1
            self.tasks.pop(taskIndex - 1)
        else:
            print("Unable to remove task, try again.")

    def updateTasksComplete(self, taskStatus: bool):
        if taskStatus is True:
            self.tasksComplete += 1
        else:
            self.tasksComplete -= 1