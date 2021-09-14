import os


class SwachhDefrag:
    def __init__(self):
        self.command = None

    def execute_disk_defragmenter(self):
        try:
            print("Starting disk defragmenter")
            self.command = os.system("defrag /c")
            print("Disk defragmentation successfully completed")
        except Exception as ex:
            print("Error running Disk defragmentation command" .format(ex))
