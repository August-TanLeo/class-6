import os
import shutil

path = '/Users/tanmaygupta/Downloads'
print("before copying files")
print(os.listdir(path))

from_directory = "/Users/tanmaygupta/Downloads"
to_directory = "/Users/tanmaygupta/Downloads/Downloaded_documents"
list_of_files = os.listdir(from_directory)

for file_name in list_of_files:
    root, ext = os.path.splitext(file_name)
    print(root)
    print(ext)

    if ext == '':
        continue

    if ext in ['.docx', '.pdf', '.PDF']:
        path1 = from_directory + '/' + file_name
        path2 = to_directory + '/' + "documents"
        path3 = to_directory + '/' + "documents" + '/' + file_name
        if os.path.exists(path2):
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            shutil.move(path1,path3)