class Tasks:
    # tasks constructor
    def __init__(self):
        self.tasks_list = []
        # constructor code here
        print("Object Created")

    # tasks destructor
    def __del__(self):
        # destructor code here
        print("Object Destroyed")
        
    def filterStatus(self, status):
        for task in self.tasks_list:
            if (task.status == False and status == False):
                print(task.title)
            
            if (task.status == True and status == True):
                print(task.title)


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

