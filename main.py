from Task import Task
from Day import Day
from User import User
from Display import *
from datetime import date


def main():
    print("TaskTracker v1.1")

    # removed account functionality, only supports single user now
    currentUser = User('Christian Madajski', 'cmad7317@tutanota.com')
    mainLoopContinue = True

    # determine if current day already has tasks or hasn't been created yet
    today = date.today()
    currentDate = today.strftime('%m/%d/%Y')
    dayIndex: int
    # serach through days to see if one already exists for the current day
    if len(currentUser.days) < 1:
        # make a new Day instance
        currentUser.days.append(Day(currentDate))
        dayIndex = 0
        print(f"Created new day instance for {currentUser.days[dayIndex].date} (from empty list)")
    else:
        dayExists: bool = False
        for count, value in enumerate(currentUser.days):
            if value.date == currentDate:
                dayIndex = count
                dayExists = True
        if dayExists:
            print(f"Accessed existing day instance for {currentUser.days[dayIndex].date}")
        else:
            # append new day instance to the end of the days list
            currentUser.days.append(Day(currentDate))
            print(f"Created new day instance for {currentUser.days[dayIndex].date} (added to existing list)")

    # MAIN PROGRAM LOOP
    while mainLoopContinue:
        mainInput = input(">> ")
        mainInputList = mainInput.split()
        # default case
        if len(mainInputList) == 0:
            print("No command entered. Try again...")
        elif mainInputList[0] == "help":
            helpMenu()
        elif mainInputList[0] == "add":
            # default case
            if len(mainInputList) == 1:
                # ask user for the new task's name
                newTaskName = input("Enter a name for the new task >> ")
                newTaskRank = len(currentUser.days.tasks) + 1
                currentUser.days[dayIndex].addTask(Task(newTaskName, newTaskRank))
            else:
                mainInputList.remove(mainInputList[0])
                newTaskName = " ".join(mainInputList)
                newTaskRank = len(currentUser.days[dayIndex].tasks) + 1
                currentUser.days[dayIndex].addTask(Task(newTaskName, newTaskRank))

        elif mainInputList[0] == "rm":
            if len(currentUser.days[dayIndex].tasks) < 1:
                print("No tasks available to remove.")
            # default case, remove most recent task
            elif len(mainInputList) == 1:
                currentUser.days[dayIndex].removeTask(len(currentUser.days[dayIndex].tasks))

            elif mainInputList[1].isdigit():
                try:
                    currentUser.days[dayIndex].removeTask(int(mainInputList[1]))
                except IndexError:
                    print("No task at provided index.")
            else:
                print("Could not remove task. Error occurred.")

        elif mainInputList[0] == "ls":
            if len(mainInputList) == 1:
                if len(currentUser.days[dayIndex].tasks) == 0:
                    print("There are currently no tasks for the day.")
                else:
                    print(str(currentUser.days[dayIndex].tasksComplete) + "/" + str(len(currentUser.days[dayIndex].tasks)) + " tasks completed for "
                          + currentUser.days[dayIndex].date + " :")
                    for x in currentUser.days[dayIndex].tasks:
                        x.printTask()
            else:
                print("Command not recognized.")

        elif mainInputList[0] == "comp":
            if len(currentUser.days[dayIndex].tasks) == 0:
                print("No tasks available to complete")
            # default case
            elif len(mainInputList) == 1:
                # show list of tasks so user can select one
                print("Tasks for " + currentUser.days[dayIndex].date + ":")
                for x in currentUser.days[dayIndex].tasks:
                    x.printTask()
                # get task number from user
                taskNum = int(input("Enter the number of the completed task >> "))
                # task rank is always one more than task index
                taskNum -= 1
                # update task status (flips current value)
                currentUser.days[dayIndex].tasks[taskNum].updateStatus(not currentUser.days[dayIndex].tasks[taskNum].status)
                currentUser.days[dayIndex].updateTasksComplete(currentUser.days[dayIndex].tasks[taskNum].status)
            elif mainInputList[1].isdigit():
                taskNum = int(mainInputList[1]) - 1
                # update task status (flips current value)
                currentUser.days[dayIndex].tasks[taskNum].updateStatus(not currentUser.days[dayIndex].tasks[taskNum].status)
                currentUser.days[dayIndex].updateTasksComplete(currentUser.days[dayIndex].tasks[taskNum].status)

        elif mainInputList[0] == "user":
            # default to printing current account info
            if len(mainInputList) == 1:
                print(f"Name: {currentUser.name}")
                print(f"Email: {currentUser.email}")
            # show all accounts
            else:
                print("Command not valid, try again.")

        elif mainInputList[0] == "exit":
            mainLoopContinue = False

        else:
            print("Command not recognized. Use HELP to see command options")

    # write task data to new file


if __name__ == '__main__':
    main()