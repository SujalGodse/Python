import os
# print(os.getcwd())

# os.chdir("D:\Python\Function")
# os.popen("Assignment")
# os.mkdir("New")
# os.rmdir("New")
# os.remove()
# print(os.listdir())
# print(os.path.exists("D:\Python\Function\Assignment.py"))
# os.rename("New","Newer")


#example on getcwd()
# print(os.getcwd())


#example on chdir()
# os.chdir(r"D:\Python")
# print(os.getcwd())

#example on popen()
# os.chdir(r"D:\Python")
# os.popen("demo.txt")
# os.popen("pic.png")

# example on mkdir()
# os.chdir(r"D:\Python")
# os.mkdir("afternoon")

#example on creating a existing folder/same folder name
# os.chdir(r"D:\Python")
# os.mkdir("afternoon")
# FileExistsError: [WinError 183] Cannot create a file when that file already exists: 'afternoon'

#example on creating 5 folders
# fname = ['mon', 'tue', 'wed', 'thu', 'fri']
# os.chdir(r"D:\Python")
# for name in fname:
#     os.mkdir(name)

#example on rmdir()
# os.chdir(r"D:\Python")
# os.rmdir("mon")
# os.rmdir("demo.txt")
# os.chdir(r"E:\mrng_file")
# os.rmdir("mon")
# FileNotFoundError: [WinError 2] The system cannot find the file specified: 'mon'

# example on remove()
# os.chdir(r"D:\Python")
# os.remove("demo.txt")
# os.remove("pic.png")

#example on listdir()
# os.chdir(r"D:\Python")
# print(os.listdir())
#['demo.txt', 'fri', 'pic.png', 'thu', 'tue', 'wed']

#example on os.path.exists()
# print(os.path.exists("D:\Python\demo.txt"))
# #True
# print(os.path.exists("D:\Python\fri"))
# #False

#example on rename()
# os.chdir(r"D:\Python")
# print(os.listdir())
#['demo.txt', 'fri', 'pic.png', 'thu', 'tue', 'wed']
# os.rename("", "friday")
# print(os.listdir())         #['fri', 'pic.png', 'sample.txt', 'thu', 'tue', 'wed']


# 1.creating a file:
# ******************
# *to create a file we use the open() method with "x" mode.
# os.chdir(r"D:\Python\File Handling")
# #without context 
# file = open("sample.txt", "x")
#creating docx file 
# file = open("dim.docx", "x")
#creating image file 
# file= open("pic.jpeg", "x")
# #with context 
# with open("demo.txt", "x") as file:
#     ...


# 2.reading a file:
# *****************

#without context
os.chdir(r"D:\Python\File Handling")

#example on file object
# file = open("sample.txt", "r")
# print(file)
#<_io.TextIOWrapper name='sample.txt' mode='r' encoding='cp1252'>
#converting file_object to list
# file = open("sample.txt", "r")
# print(list(file))
#['day without class a day is best day\n', 'guys be interactive\n','tomato is to costly\n', 'same house and husband boring.']
#run for loop for file object
# file = open("sample.txt", "r")
# for i in file:
#     print(i.rstrip("\n"))


#example on read() method
# file = open("sample.txt")
# print(file.read())


#example on readline()
# file = open("sample.txt")
# print(file.readline())
#day without class a day is best day
#example on readlines()
# file = open("sample.txt")
# print(file.readlines())
# #['day without class a day is best day\n', 'guys be interactive\n', 'tomato is to costly\n', 'same house and husband boring.\n']

# 3.writing into a file:
# **********************
# example on writing into existing file
# with open("sample.txt", "w") as file:
#     file.write("today is tuesday")

# example on writing into not existing file
# with open("sample12.txt", "w") as file:
#     file.write("today is tuesday")

# writing multiple lines in existing file
# with open("sample.txt", "w") as file:
#     file.writelines(["hai\n", "hello\n", "how\n", "bye\n"])
#     l.append(line.split()[0] + "\n")
#
# with open("sample.txt", "w") as file:
#   file.writelines(l)

# 4.appending into a file:
# ************************

#appending to a existing file
# with open("sample.txt", "a") as file:
#     file.write("Mahesh 77\n")
#appending to a file not exists
# with open("sample12.txt", "a") as file:
#     file.writelines(["Lokesh 77\n", "Kumar 59\n", "Rum 99\n"])


from csv import *
# with open("demo.txt") as file_obj:
#     data =csv. Dictreader(file_obj)
