from Task import Task
from Day import Day
from Account import Account
from Display import *
from datetime import date


def main():
    print("TaskTracker v1.0")

    # read account information from accounts.txt
    accounts: list[Account] = []
    readFile = open("accounts.txt", "r")
    linesRead = 0
    currLine = readFile.readline()
    while currLine:
        splitLine = currLine.split()
        accounts.append(Account(splitLine[0], splitLine[1], splitLine[2]))
        linesRead += 1
        currLine = readFile.readline()
    readFile.close()
    print("Accounts loaded from memory: " + str(linesRead) + "\n")

    # AUTHENTICATION
    emailValid = False
    passwordValid = False
    loginSuccess = False
    mainLoopContinue = False
    accountIndex: int = 0

    while not loginSuccess:
        # get user email and password
        attemptEmail: str = input("Email: ")
        attemptPassword: str = input("Password: ")
        # allow for users to exit program from log-in
        if attemptPassword == 'exit' or attemptEmail == 'exit':
            break
        # check if email is valid
        if len(accounts) > 0:
            for x in range(0, len(accounts) - 1):
                if accounts[x].email == attemptEmail:
                    emailValid = True
                    accountIndex = x
                    break
        # if the email provided exists in the database
        if emailValid is True:
            # check if password for the given email is valid
            if accounts[accountIndex].password == attemptPassword:
                passwordValid = True
                print("Log-in successful\n")
            else:
                print("Incorrect password, try again.\n")
        # if the email provided does not exist in the database
        else:
            print("Email does not exist, try again.\n")
        if emailValid and passwordValid:
            loginSuccess = True

    if loginSuccess:
        mainLoopContinue = True

    # set the working account to the account associated to the provided email
    currAccount = accounts[accountIndex]

    # determine if current day already has tasks or hasn't been created yet
    today = date.today()
    currDate = today.strftime('%m/%d/%Y')
    dayIndex: int
    # serach through days to see if one already exists for the current day
    if len(currAccount.days) > 0:
        dayFound = False
        for x in range(0, len(currAccount.days)):
            if currAccount.days[x].date == currDate:
                dayFound = True
                dayIndex = x
                currDay = currAccount.days[dayIndex]
        # if no day is found, then make a new day
        if dayFound:
            currAccount.days.append(Day(currDate))
            currDay = currAccount.days[len(currAccount.days) - 1]
    # if no days exist, just make a new day
    else:
        currAccount.days.append(Day(currDate))
        currDay = currAccount.days[0]
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
                try:
                    currDay.removeTask(int(mainInputList[1]))
                except IndexError:
                    print("No task at provided index.")
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

        elif mainInputList[0] == "acc":
            if len(mainInputList) == 1:
                 # print current account info
                print("Name: ", accounts[currDay].name)
                print("Email: ", accounts[currDay].email)
            else:
                print("Too many arguments, try again.")

        elif mainInputList[0] == "exit":
            mainLoopContinue = False

        else:
            print("Command not recognized. Use HELP to see command options")


if __name__ == '__main__':
    main()