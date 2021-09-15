import os
from logger import logger


class SwachhDefrag:
    def __init__(self):
        self.command = None

    def execute_chkdisk(self):
        try:
            logger.info("CHKDSK started")
            self.command = os.system("chkdsk /f*")
        except Exception as ex:
            logger.error(ex)

    def execute_disk_defragmenter(self):
        try:
            logger.info("Disk defermentation started")
            self.command = os.system("defrag /C /H")
        except Exception as ex:
            logger.error("Error running Disk defragmentation command" .format(ex))
