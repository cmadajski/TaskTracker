

def helpMenu():
    print("List of Common Commands:")
    print("  USER - shows current user information")
    print("  ADD - adds a new task for the current day")
    print("  RM - removes a task from the current day")
    print("  LS - list all tasks for the current day")
    print("  COMP - mark/unmark a task as completed")
    print("  EXIT - terminate the program")

def add_help():
    print('Help for ADD command')
    print('  ADD - asks user to provide a new task name before creating new task')
    print('  ADD [taskname] - adds a new task with the provided name')
    print('  ADD HELP - prints the help menu for the ADD command')

def rm_help():
    print('Help for RM command')
    print('  RM - removes the most recently made task from the current day')
    print('  RM [taskindex] - removes the task at the given index value for the current day')
    print('  RM HELP - prints the help menu for the RM command')