from Task import Task
from Day import Day
from Account import Account
from Display import *
from datetime import date


def main():
    print("TaskTracker v1.0")

    # placeholder account info
    accounts: list[Account] = []
    accounts.append(Account("Christian", "cmad7317@gmail.com", "password6318!"))
    accounts.append(Account("generic", "generic@gmail.com", "generic1234!"))
    accounts.append(Account("joestar", "jojo@jojo.com", "jojojo"))


    # AUTHENTICATION
    emailValid = False
    passwordValid = False
    loginSuccess = False

    while not emailValid:
        attemptEmail: str = input("Enter an email: ")
        # search accounts to see if username exists
        if attemptEmail == "exit":
            break
        i: int = 0
        accountIndex: int = 0
        while i < len(accounts):
            if accounts[i].email == attemptEmail:
                emailValid = True
                print("Email is valid.")
                accountIndex = i
                i = len(accounts)
            else:
                i += 1
        if not emailValid:
            print("Email not recognized, try again.")

    while not passwordValid:
        attemptPassword: str = input("Enter password: ")
        # check if password is valid
        if accounts[accountIndex].password == attemptPassword:
            passwordValid = True
            print("Password valid.")
        else:
            print("Password not valid, try again.")




    if loginSuccess is False:
        mainLoopContinue = False
    else:
        mainLoopContinue = True

    # determine if current day already has tasks or hasn't been created yet
    today = date.today()
    # serach through

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

        elif mainInputList[0] == "acc":
            if len(mainInputList) == 1:
                 # print current account info
                print("Name: ", person.name)
                print("Email: ", person.email)
            else:
                print("Too many arguments, try again.")

        elif mainInputList[0] == "exit":
            mainLoopContinue = False

        else:
            print("Command not recognized. Use HELP to see command options")


if __name__ == '__main__':
    main()