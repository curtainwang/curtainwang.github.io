import os
import platform

# generate my site's files

dir="./"
for root, dirs, files in os.walk(dir):
	for file in files:
		print os.path.join(root, file)

# write the answer to a text file
dir="."
g_file="file.txt"

for root, dirs, files in os.walk(dir, topdown=False):
	for file in files:
		print os.path.join(root, file)

f=open(r'./file.txt', 'w')
f.write('hello')
f.writelines(['nihao', 'sb'])


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
