# برای خواندن و یا نوشتن دیتا روی فایل لازم است آن را ابتدا باز کنیم
#  و نهایتا پس از استفاده باید بسته شود
#  تا منابعی که برای برای کار با فایل درگیر شده‌اند آزاد شوند

# 1- باز کردن فایل
# 2- خواندن یا نوشتن (انجام عملیات)
# 3- بستن فایل

# باز کردن فایل 
# Open returns an object to be used for read/write
f = open("test1.txt")    # open file in current directory
f = open("C:/test2.txt")  # specifying full path; for longer path: f = open("c:/abc/def/test2.txt")
f = open("C:\\test2.txt") # another way with using two backslash; for longer path: f = open("c:\\abc\\def\\test2.txt")


# آدرس فایل و پوشه
##################################################################
# current working directory
import os # The OS module provides functions for interacting with operating system. 
current_working_dir = os.getcwd()
print(current_working_dir)

# change working directory
import os
print("Old cwd = " + os.getcwd())
os.chdir("C:\\")
print("New cwd = " + os.getcwd())
# os.chdir("C:\\PythonProgramming")

# create absolute path of a file
abs_pathname = os.path.join(current_working_dir, "test1.txt")
print(abs_pathname)

# get absolute path of the current python file
import os
absolutepath = os.path.abspath(__file__)
print(absolutepath)

# relative path
absolutepath = os.path.abspath(__file__)
print(absolutepath)

fileDirectory = os.path.dirname(absolutepath)
print(fileDirectory)
# Path of parent directory
parentDirectory = os.path.dirname(fileDirectory)
print(parentDirectory)
# Navigate to "windows" directory
newPath = os.path.join(parentDirectory, 'windows')   
print(newPath)

# open a file in parent directory
print(os.path.abspath("../"))
f = open("..\\test2.txt")

# some other os functions
# os.mkdir: create directory
# os.listdir: list of files and folders in a directory
##################################################################


# هنگام باز کردن فایل حالت  کار با فایل را نیز مشخص کنیم

# r  => فایل برای خواندن باز می‌کند (پیش فرض)

# w  => فایل را برای نوشتن باز می‌کند. اگر فایلی وجود نداشته باشد، فایل جدیدی ایجاد می‌کند در غیر اینصورت محتوای فایل بدون حذف کردن فایل پاک می‌شود و فایل را آماده نوشتن می‌کند

# x  => فایل را برای نوشتن ایجاد می‌کند. اگر فایلی وجود داشته باشد، خطای زیر را می‌دهد
#               FileExistsError
# برای مواقعی که میخواهیم مطمئن شویم فایل اوررایت نمیشود مفید است

# a  => فایل را برای نوشتن باز می‌کند. اگر فایلی وجود نداشته باشد، فایل جدیدی ایجاد می‌کند در غیر اینصورت فایل را برای افزودن دیتا به انتهای آن آماده نوشتن می‌کند

# t  => باز کردن فایل در حالت متن (پیش فرض)
# b  => باز کردن فایل در حالت باینری، حالت باینری برای فایل های غیرمتنی مثل تصویر است
# +  => باز کردن فایل برای خواندن و نوشتن به صورت همزمان 

absolutepath = os.path.abspath(__file__)
os.chdir(os.path.dirname(absolutepath))

f = open("test1.txt")      # equivalent to 'r' or 'rt'
f = open("test4.txt",'w')  # write in text mode and overwrite
f = open("img1.bmp",'w+b') # read and write in binary mode and overwrite

# بسبتن فایل
f = open("test1.txt", encoding = 'utf-8')
f.close()

# open file, do operations. Then file closes automatically (no need to file.close())
with open("test1.txt", encoding = 'utf-8') as f:
   # perform file operations
   pass

# نوشتن در فایل
with open("test3.txt",'w',encoding = 'utf-8') as f:
   f.write("This is\n")
   f.write("my first file\n")
   f.write("This file\n")
   f.write("contains four lines\n")
# f.close() is not required

# writelines
f = open("test3.txt","a")
L = ["abcd\n", "efgh\n", "ijkl\n"] 
f.writelines(L)
f.close()


# خواندن ار فایل
f = open("test1.txt",'r',encoding = 'utf-8')
print(f.read(4))    #  خواندن 4 کاراکتر اول

print(f.read(4))    # خواندن 4 کاراکتر بعدی

print(f.read())     # خواندن باقی خطوط

print(f.read())  # خواندن بعدی تنها یک رشته خالی برمی‌گرداند

f.close()

# readline()
# خواندن یک خط از فایل
f = open("test1.txt",'r')
print(f.readline())
print(f.readline())
f.close()

# readlines()
f = open("test1.txt",'r')
print(f.readlines())
f.close()

# روش دیگر خواندن محتویات فایل
f = open("test1.txt",'r')
for line in f:
	print(line , end = '')
    # How print contents in a single line? print(line[:-1] , end = '')
f.close()
print(" ")

# seek method
f = open("test1.txt", "r")
f.seek(4)
print(f.readline())
f.seek(0)
print(f.readline())

# read binary file
f = open("img1.bmp","rb")
print(f.read())

# read a file which does not exist
# f = open("test10.txt",'r') # error


