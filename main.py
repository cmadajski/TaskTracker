from Task import *
from Day import *
from datetime import date


def main():
    mainLoopContinue = True
    currDay = Day()
    # taskList: list[Task] = []
    # today = date.today()
    # todayStr = today.strftime('%m/%d/%Y')

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
                newTaskRank = len(currDay.tasks) + 1
                currDay.addTask(Task(newTaskName, newTaskRank))

        elif mainInputList[0] == "ls":
            if len(mainInputList) == 1:
                if len(currDay.tasks) == 0:
                    print("There are currently no tasks for the day.")
                else:
                    print(str(currDay.tasksComplete) + "/" + str(len(currDay.tasks)) + " tasks completed for "
                          + currDay.date + " :")
                    for x in currDay.tasks:
                        x.printTask()

        elif mainInputList[0] == "comp":
            if len(currDay.tasks) == 0:
                print("No tasks available to complete")
            # default case
            elif len(mainInputList) == 1:
                # show list of tasks so user can select one
                print("Tasks for " + currDay.date + ":")
                for x in currDay.tasks:
                    x.printTask()
                # get task number from user
                taskNum = int(input("Enter number of the completed task >> "))
                # task rank is always one more than task index
                taskNum -= 1
                # update task status (flips current value)
                currDay.tasks[taskNum].updateStatus(not currDay.tasks[taskNum].status)
                currDay.updateTasksComplete(currDay.tasks[taskNum].status)
            elif mainInputList[1].isdigit():
                taskNum = int(mainInputList[1]) - 1
                # update task status (flips current value)
                currDay.tasks[taskNum].updateStatus(not currDay.tasks[taskNum].status)
                currDay.updateTasksComplete(currDay.tasks[taskNum].status)

        elif mainInputList[0] == "exit":
            mainLoopContinue = False

        else:
            print("Command not recognized. Use HELP to see command options")


if __name__ == '__main__':
    main()