class Tasks:
    # tasks constructor
    def __init__(self):
        # constructor code here
        print("Object Created")

    # tasks destructor
    def __del__(self):
        # destructor code here
        print("Object Destroyed")


class Task:
   
    # task constructor
    def __init__(self):
        # constructor code here
        print("Object Created")
        self.status = False

    # task destructor
    def __del__(self):
        # destructor code here
        print("Object Destroyed")

    def edit(self):
        print("Editing Task")
        # edit code here

    def delete(self):
        print("Deleting Task")
        # delete code here

    def toggle_status(self):
        self.status = not self.status    
        print("Task Complete")
        # mark_complete code here
