#WAP to print the contents of a directory using the os module
# print("hello")
import os
# files = os.listdir( ) 
# print(files)
# #to get the current working directory
# print(os.getcwd())
# # use os module to create a folder in current working directory

# # os.mkdir("bm")
# #path exists in new directory true or false
# print(os.path.exists("new_folder"))
# print(os.path.exists("new"))

# #rename folder
# os.rename("new_folder","hiii")

#if a file exists
print(os.path.isfile("mod.py"))

#if dir exists
print(os.path.isdir("new_folder"))

#remove file
print(os.remove("mod.py"))