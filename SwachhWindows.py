from SwachhFiles import SwachhFiles


class SwachhWindows:
    @staticmethod
    def main():
        my_tempfiless = SwachhFiles()
        my_tempfiless.delete_temp_files()
        my_tempfiless.empty_recycle_bin()
        my_tempfiless.delete_files_with_pattern()
        my_tempfiless.delete_defender_files()
        my_tempfiless.delete_win_error_reporting_files()
        my_tempfiless.delete_single_files()


if __name__ == "__main__":
    SwachhWindows.main()


