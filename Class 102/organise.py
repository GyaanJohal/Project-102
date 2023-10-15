import os
import shutil
source ="C:/Users/gjoha/Downloads"
destination ="C:/Users/gjoha/OneDrive/Documents/Out of School/Visual Studio Code/BYJUS/Python/Class 102"
list_of_files = os.listdir(source)
print(list_of_files)

for file_name in list_of_files:
    name, ext = os.path.splitext(file_name)
    print(name)
    print(ext)
    if ext == "":
        continue
    if ext in ['.gif', '.png', '.jpg', '.jpeg', '.jfif', '.bmp']:
        path1 = source + '/' + file_name
        path2 = destination + '/' + 'Image_files'
        path3 = destination + '/' + 'Image_files' + '/' + file_name
        print(path1)
        print(path3)
         
        if os.path.exists(path2):
            print("Moving " + file_name + ".....")
            shutil.move(path1, path3)
        else:
            os.mkdir(path2)
            print("Moving " + file_name + ".....")
            shutil.move(path1, path3)
