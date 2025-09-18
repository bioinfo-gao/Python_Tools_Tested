import os

path = "data"

# i=1
# print(f"The Current cycle count i is : {i}")
# print("\n")
# for filepath, folder, files in os.walk(path):
#     print(f"The Current cycle count i is : {i}")
#     print(filepath)
#     print(files)
#     j=1
#     for file in files:
#         print(f"The Current cycle count i is : {i} and the Current j is {j}")
#         print(os.path.join(filepath,file))
#         j += 1
#     i += 1
#     print("============ separator between i =========== ")

for files in os.listdir(path):

    print(files)
