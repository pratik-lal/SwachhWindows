import os
import shutil
import glob


class ChildItem:
    def __init__(self, filepath):
        self.filepath = filepath

    def delete_childitems(self):
        files = glob.glob(self.filepath)
        for each_file in files:
            try:
                if os.path.isdir(each_file):
                    print("Deleted folder and it contents: {}" .format(each_file))
                    shutil.rmtree(each_file)
                elif os.path.isfile(each_file) or os.path.islink(each_file):
                    print("Deleted file: {}" .format(each_file))
                    os.remove(each_file)
                else:
                    pass
            except Exception as ex:
                print("Error in delete_childitems method")
                print(ex)
