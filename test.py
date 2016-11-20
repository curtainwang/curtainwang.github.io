import os
import platform

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
	generate_file = open(file_name, 'w') 

	for file in os.listdir(dir_name):
		generate_file.write(file)
		generate_file.write('\n')

	generate_file.close()
	return



get_file("./html/", "file_html.txt")
get_file("./txt/", "file_txt.txt")

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