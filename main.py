from Task import *
from Day import *
from datetime import date


def main():
    mainLoopContinue = True
    currDay = Day()

    while mainLoopContinue:
        mainInput = input(">> ")
        mainInputList = mainInput.split()
        # default case
        if len(mainInputList) == 0:
            print("No command entered. Try again...")
        elif mainInputList[0] == "add":
            # default case
            if len(mainInputList) == 1:
                # ask user for the new task's name
                newTaskName = input("Enter a name for the new task >> ")
                newTaskRank = len(currDay.tasks) + 1
                currDay.addTask(Task(newTaskName, newTaskRank))
            else:
                mainInputList.remove(mainInputList[0])
                newTaskName = " ".join(mainInputList)
                newTaskRank = len(currDay.tasks) + 1
                currDay.addTask(Task(newTaskName, newTaskRank))

        elif mainInputList[0] == "rm":
            if len(currDay.tasks) < 1:
                print("No tasks available to remove.")
            # default case, remove most recent task
            elif len(mainInputList) == 1:
                currDay.removeTask(len(currDay.tasks))
            elif mainInputList[1].isdigit():
                currDay.removeTask(int(mainInputList[1]))
            else:
                print("Could not remove task. Error occurred.")

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
                taskNum = int(input("Enter the number of the completed task >> "))
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