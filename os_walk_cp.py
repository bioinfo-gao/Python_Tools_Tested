import os
import shutil
#from copy import copy # 这个 copy 是 Python 内置的 copy 模块中的函数，用于复制 Python 对象（如列表、字典、自定义类实例等），不是用来复制文件的！

current_dir = os.getcwd()
new_dir_name = "backup_folder\docx"
new_dir_path = os.path.join(current_dir, new_dir_name)
os.makedirs(new_dir_path, exist_ok=True)  # exist_ok=True 避免目录已存在时报错

path = "data"

for filepath, folder, files in os.walk(path):

    for file in files:
        if '.txt' in file:
            print(os.path.join(filepath,file))
            print(os.path.getsize(os.path.join(filepath,file)))
            print(os.path.join(new_dir_path, file) ) #os.path.join(r"backup_folder\docx", file)
            #shutil.copy2(os.path.join(filepath,file), os.path.join(new_dir_path, file))#os.path.join(r"backup_folder\docx", file)


