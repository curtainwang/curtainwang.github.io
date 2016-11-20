#coding=utf-8

import os
import sys
import time
import platform

default_encoding = "utf-8";

'''
dir="./"
f=open(r'./file.txt', 'w') #g_file="file.txt"


# generate my site's files
for root, dirs, files in os.walk(dir):
	for file in files:
		print os.path.join(root, file)


for root, dirs, files in os.walk(dir, topdown=False):
	for file in files:
		print os.path.join(root, file)


f.write('hello')
f.writelines(['nihao', 'sb'])
f.close()
'''

def get_file(dir_name, file_name):
	
	#generate_file.decode
	
	for file in os.listdir(dir_name):
		generate_file.write(file)
		generate_file.write('|')

	
	return

file_name = "website_list.txt"
generate_file = open(file_name, 'w') 

get_file("./html/", file_name)
get_file("./txt/", file_name)

generate_file.close()

# now commit
cmd = "git add . & "
cmd += 'git commit -m "'+ time.strftime('%Y-%m-%d %H:%M:%S') + '" & git push'
os.system(cmd)

'''
# check the operating system
if platform.system() == "Windows":
	print("this is windows")
elif
	print("this is linux")


# make the command line for committing
cmd = " & \
git add . & \
set tmp=%date:~0,10% %time:~0,8% & \
git commit -m "%tmp%" & \
git push & \
"
os.system(cmd)

os.system("git add .")
os.system("set tmp=%date:~0,10% %time:~0,8%")
os.system("git commit -m "%tmp%"")
os.system("git push")
'''