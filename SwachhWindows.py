from SwachhFiles import SwachhFiles
from logger import logger
from SwachhDefrag import SwachhDefrag


class SwachhWindows:
    @staticmethod
    def main():
        my_tempfiles = SwachhFiles()
        my_tempfiles.delete_temp_files()
        my_tempfiles.empty_recycle_bin()
        my_tempfiles.delete_files_with_pattern()
        my_tempfiles.delete_windows_upgrade_files()

        disk_defrag = SwachhDefrag()
        disk_defrag.execute_disk_defragmenter()


if __name__ == "__main__":
    logger.info("Executing Main Program")
    SwachhWindows.main()


