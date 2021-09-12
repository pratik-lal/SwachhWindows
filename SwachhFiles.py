import os
import winshell
from SwachhChildItems import ChildItem


class SwachhFiles:
    def __init__(self):
        self.temp_folder = os.environ.get("TEMP")
        self.windir_folder = os.environ.get("WINDIR")
        self.programdata_folder = os.environ.get("PROGRAMDATA")
        self.user_profile_folder = os.environ.get("USERPROFILE")
        self.all_user_profiles = os.environ.get("ALLUSERSPROFILE")
        self.recycle_bin_folder = winshell.recycle_bin()

    def delete_temp_files(self):
        setuplog_txtfiles = self.windir_folder + "\\\\setuplog.txt"
        win32_ntlog_files = self.windir_folder + "\\\\winnt32.log"
        single_files: list = [setuplog_txtfiles, win32_ntlog_files]
        for each_file in single_files:
            try:
                os.remove(each_file)
                print("Successfully delete single file {}".format(each_file))
            except Exception as ex:
                print("Unable to delete single file: delete_single_files {}".format(each_file))
                print(ex)

    def empty_recycle_bin(self):
        try:
            self.recycle_bin_folder.empty(confirm=False, show_progress=False, sound=False)
            print("Successfully deleted files from Recycle Bin")
        except Exception as ex:
            print("Error deleting recycle bin files")
            print(ex)

    def delete_files_with_pattern(self):
        windir_temp_folder = self.windir_folder + "\\\\Temp\\\\*"
        windir_logs_folder = self.windir_folder + "\\\\Logs\\\\*"
        windir_sys32_logfiles_folder = self.windir_folder + "\\\\System32\\\\LogFiles\\\\*"
        diagnostic_dataviewer_dbfiles = self.programdata_folder + "\\\\Microsoft\\\\Diagnosis\\\\EventTranscript\\\\*"
        user_downloads_folder = self.user_profile_folder + "\\\\Downloads\\\\*"
        feedbackhub_archive_logfiles_folder = self.programdata_folder + "\\\\Microsoft\\\\Diagnosis\\\\FeedbackArchive\\\\*"
        setuplog_files = self.windir_folder + "\\\\setup*.log"
        setuplog_old_files = self.windir_folder + "\\\\setup*.old"
        sys_error_memory_dump_files = self.windir_folder + "\\\\*.dmp"
        sys_error_minidump_files = self.windir_folder + "\\\\Minidump\\\\*.dmp"
        win_defender_localcopy_files = self.programdata_folder + "\\\\Microsoft\\\\Windows Defender\\\\LocalCopy\\\\*"
        win_defender_support_files = self.programdata_folder + "\\\\Microsoft\\\\Windows Defender\\\\Support\\\\*"
        win_error_reporting_files = self.all_user_profiles + "\\\\Microsoft\\\\Windows\\\\WER\\\\*"
        active_setup_temp_folders = self.windir_folder + "\\\\msdownld.tmp\\\\*.tmp"
        content_index_cleaner_folder = "C:\\\\Catalog.wci\\\\.*"

        files_with_pattern: list = [windir_temp_folder,
                                    windir_logs_folder,
                                    windir_sys32_logfiles_folder,
                                    diagnostic_dataviewer_dbfiles,
                                    user_downloads_folder,
                                    feedbackhub_archive_logfiles_folder,
                                    setuplog_files, setuplog_old_files,
                                    sys_error_memory_dump_files,
                                    sys_error_minidump_files,
                                    win_defender_localcopy_files,
                                    win_defender_support_files,
                                    win_error_reporting_files,
                                    active_setup_temp_folders,
                                    content_index_cleaner_folder]

        for each_item in files_with_pattern:
            ChildItem(each_item).delete_childitems()

    @staticmethod
    def delete_windows_upgrade_files():
        files = ["C:\\Windows\\Panther\\Setupact.log",
                 "C:\\Windows\\panther\\setuperr.log",
                 "C:\\Windows\\inf\\setupapi.app.log",
                 "C:\\Windows\\inf\\setupapi.app.log",
                 "C:\\Windows\\inf\\setupapi.dev.log",
                 "C:\\Windows\\panther\\PreGatherPnPList.log",
                 "C:\\Windows\\panther\\PostApplyPnPList.log",
                 "C:\\Windows\\panther\\miglog.xml",
                 "C:\\Windows\\setupapi.log",
                 "C:\\Windows\\Logs\\MoSetup\\BlueBox.log",
                 "C:\\Windows\\panther\\miglog.xml",
                 "C:\\Windows\\memory.dmp"]
        for each_file in files:
            try:
                os.remove(each_file)
                print("Successfully removed file {}" .format(each_file))
            except Exception as ex:
                print("Error in delete_windows_upgrade_files()")
                print(ex)
