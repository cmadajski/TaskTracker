from datetime import date
from Task import Task


class Day:

    tasks: list[Task] = []
    date: str
    tasksComplete: int
    numTasks: int

    def __init__(self, inDate: str):
        self.date = inDate
        self.tasksComplete = 0
        self.numTasks = 0

    def addTask(self, inTask: Task):
        self.tasks.append(inTask)
        if inTask.completed is True:
            self.tasksComplete += 1
        self.numTasks += 1

    def removeTask(self, inputVal: int):
        # translate task number to index number
        index = int(inputVal) - 1
        self.numTasks -= 1
        if self.tasks[index].completed is True:
            self.tasksComplete -= 1
        self.tasks.pop(index)
        # shift rank numbers for all tasks following the removed task
        for x in range(index, len(self.tasks)):
            self.tasks[x].rank -= 1

    def setCompleted(self, taskCompleted: bool):
        if taskCompleted is True:
            self.tasksComplete += 1
        else:
            self.tasksComplete -= 1

    def printTasks(self):
        print(f"Total number of tasks for {self.date}: {self.numTasks}")
        for x in self.tasks:
            x.printTask()