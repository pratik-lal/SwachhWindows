import os
import shutil
import winshell
import glob


class SwachhFiles:
    def __init__(self):
        self.temp_folder = os.environ.get("TEMP")
        self.windir_folder = os.environ.get("WINDIR")
        self.programdata_folder = os.environ.get("PROGRAMDATA")
        self.user_profile_folder = os.environ.get("USERPROFILE")
        self.all_user_profiles = os.environ.get("ALLUSERSPROFILE")
        self.recycle_bin_folder = winshell.recycle_bin()

    def delete_temp_files(self):
        windir_temp_folder = self.windir_folder + "\\Temp"
        windir_logs_folder = self.windir_folder + "\\Logs"
        windir_sys32_logfiles_folder = self.windir_folder + "\\System32\\LogFiles"
        active_setup_temp_folders = self.windir_folder + "\\msdownld.tmp"
        diagnostic_dataviewer_dbfiles = self.programdata_folder + "\\Microsoft\\Diagnosis\\EventTranscript"
        user_downloads_folder = self.user_profile_folder + "\\Downloads"
        feedbackhub_archive_logfiles_folder = self.programdata_folder + "\\Microsoft\\Diagnosis\\FeedbackArchive"

        temp_folders: list = [self.temp_folder, windir_temp_folder, windir_logs_folder, windir_sys32_logfiles_folder,
                              active_setup_temp_folders, diagnostic_dataviewer_dbfiles, user_downloads_folder,
                              feedbackhub_archive_logfiles_folder]
        for each_file_folders in temp_folders:
            try:
                print("Successfully deleted files and folders from path: {}".format(each_file_folders))
                shutil.rmtree(each_file_folders)
            except Exception as ex:
                print("Error deleting temp folders {}" .format(each_file_folders))
                print(ex)

    def empty_recycle_bin(self):
        try:
            self.recycle_bin_folder.empty(confirm=False, show_progress=False, sound=False)
            print("Successfully deleted files from Recycle Bin")
        except Exception as ex:
            print("Error deleting recycle bin files")
            print(ex)

    def delete_files_with_pattern(self):
        init_setuplog_files = self.windir_folder + "\\setup*.log"
        init_setuplog_old_files = self.windir_folder + "\\setup*.old"
        setuplog_files = glob.glob(init_setuplog_files, recursive=False)
        setuplog_old_files = glob.glob(init_setuplog_old_files, recursive=False)
        init_sys_error_memory_dump_files = self.windir_folder + "\\*.dmp"
        sys_error_memory_dump_files = glob.glob(init_sys_error_memory_dump_files)
        init_sys_error_minidump_files = self.windir_folder + "\\Minidump\\*.dmp"
        sys_error_minidump_files = glob.glob(init_sys_error_minidump_files, recursive=False)

        # glob already returns a list, bug fix needed below
        files_with_pattern: list = [setuplog_files, setuplog_old_files, sys_error_memory_dump_files,
                                    sys_error_minidump_files]

        for each_file in files_with_pattern:
            try:
                os.remove(each_file)
                print("Successfully deleted file {}" .format(each_file))
            except Exception as ex:
                print("Error deleting files with pattern {}" .format(each_file))
                print(ex)

    def delete_defender_files(self):
        win_defender_localcopy_files = self.programdata_folder + "\\Microsoft\\Windows Defender\\LocalCopy"
        win_defender_support_files = self.programdata_folder + "\\Microsoft\\Windows Defender\\Support"

        win_defender_files = [win_defender_localcopy_files, win_defender_support_files]
        for each_file in win_defender_files:
            try:
                shutil.rmtree(each_file)
                print("Successfully deleted Windows Defender temporary files. {}" .format(each_file))
            except Exception as ex:
                print("Error deleting defender temp folders {}" .format(each_file))
                print(ex)

    def delete_win_error_reporting_files(self):
        win_error_reporting_files = self.all_user_profiles + "\\Microsoft\\Windows\\WER"
        try:
            shutil.rmtree(win_error_reporting_files)
            print("Successfully deleted Windows error reporting files {}".format(win_error_reporting_files))
        except Exception as ex:
            print("Error deleting temp folders {}".format(win_error_reporting_files))
            print(ex)

    def delete_single_files(self):
        setuplog_txtfiles = self.windir_folder + "\\setuplog.txt"
        win32_ntlog_files = self.windir_folder + "\\winnt32.log"
        single_files: list = [setuplog_txtfiles, win32_ntlog_files]
        for each_file in single_files:
            try:
                os.remove(each_file)
                print("Successfully delete single file {}".format(each_file))
            except Exception as ex:
                print("Unable to delete single file: delete_single_files {}".format(each_file))
                print(ex)
