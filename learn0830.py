import os

def file_name(self, user_dir):
    file_list = list()
    for root, dirs, files in os.walk(user_dir):
        for file in files:
            # if os.path.splitext(file)[1] == '.txt':
            file_list.append(os.path.join(root, file))
    return file_list
all_files=file_name(1,'F:\桌面\分众监播项目\中国监播\kuma数据文档')
for all_file in all_files:
    print(all_file)

def file_name(user_dir):
    file_list = list()
    for root, dirs, files in os.walk(user_dir):
        print(root)
        print(dirs)
        print(files)
file_name('F:\桌面\分众监播项目\中国监播\kuma数据文档')
