from SwachhFiles import SwachhFiles


class SwachhWindows:
    @staticmethod
    def main():
        my_tempfiles = SwachhFiles()
        my_tempfiles.delete_temp_files()
        my_tempfiles.empty_recycle_bin()
        my_tempfiles.delete_files_with_pattern()
        my_tempfiles.delete_windows_upgrade_files()


if __name__ == "__main__":
    SwachhWindows.main()


