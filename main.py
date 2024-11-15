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
        self.title = ""
        self.status = False

    # task destructor
    def __del__(self):
        # destructor code here
        print("Object Destroyed")

    def edit(self, new_name):
        print(f"Editing Task: {self.title} to {new_name}")
        self.title = new_name
        print("Task name updated successfully.\n")

    def toggle_status(self):
        self.status = not self.status    
        print("Task Complete")