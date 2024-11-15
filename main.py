class Tasks:
    # tasks constructor
    def __init__(self):
        self.tasks_list = []

    def addtask(self, new_name):
        self.tasks_list.append(Task(new_name))

    def editTask(self, index, new_name):
        self.tasks_list[index].edit(new_name)

    def toggleTask(self, index):
        self.tasks_list[index].toggle_status()

    def filterStatus(self, status):
        index = 0
        for task in self.tasks_list:
            if (task.status == False and status == False):
                print("[" + str(index) + "]" + task.title)

            if (task.status == True and status == True):
                print("[" + str(index) + "]" + task.title)

            index = index + 1

    def deleteTask(self, index):
        self.tasks_list.pop(index)


class Task:
    # task constructor
    def __init__(self, new_name):
        # constructor code here
        self.title = new_name
        self.status = False

    def edit(self, new_name):
        self.title = new_name

    def toggle_status(self):
        self.status = not self.status


tasks = Tasks()

while (True):
    print("a - add task, c - see completed task, i - see incomplete task, d - delete task, e - edit task, m - toggle task, x - to exit")
    operation = str(input())

    if (operation == "a"):
        print("enter title: ")
        title = str(input())
        tasks.addtask(title)

    if (operation == "c"):
        tasks.filterStatus(True)

    if (operation == "i"):
        tasks.filterStatus(False)

    if (operation == "e"):
        print("enter index: ")
        index = int(input())
        print("enter new title: ")
        title = str(input())
        tasks.editTask(index, title)

    if (operation == "d"):
        print("enter index: ")
        index = int(input())
        tasks.deleteTask(index)

    if (operation == "m"):
        print("enter index: ")
        index = int(input())
        tasks.toggleTask(index)

    if (operation == "x"):
        break

    print()
