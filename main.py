from Task import *
from datetime import date


def main():
    mainLoopContinue = True
    taskList: list[Task] = []
    today = date.today()
    todayStr = today.strftime('%m/%d/%Y')

    while mainLoopContinue:
        mainInput = input(">> ")
        mainInputList = mainInput.split()
        # default case
        if len(mainInputList) == 0:
            print("No command entered. Try again...")
        elif mainInputList[0] == "add":
            # default case
            if len(mainInputList) == 1:
                print("Default case not implemented yet :(")
            else:
                mainInputList.remove(mainInputList[0])
                newTaskName = " ".join(mainInputList)
                taskList.append(Task(newTaskName))

        elif mainInputList[0] == "ls":
            if len(mainInputList) == 1:
                if len(taskList) == 0:
                    print("There are currently no tasks for the day.")
                else:
                    print("Tasks for " + todayStr + ":")
                    for x in taskList:
                        x.printTask()


if __name__ == '__main__':
    main()