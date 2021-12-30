

class Task:

    name: str
    completed: bool
    rank: int

    def __init__(self, inName, inRank):
        self.name = inName
        self.completed = False
        self.rank = inRank

    def setCompleted(self, isComplete: bool):
        self.completed = isComplete

    def setName(self, newName: str):
        self.name = newName

    def printTask(self):
        if not self.completed:
            print(f"{self.rank}. [ ] {self.name}")
        else:
            print(f"{self.rank}. [X] {self.name}")
