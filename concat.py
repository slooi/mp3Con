import os
folder_name = "combine"

if not os.path.exists(folder_name):
	os.mkdir(folder_name)

namesFile = open("filenames.txt","w")
names = ["file './{}/{}'\n".format(folder_name,filename) for filename in os.listdir("./{}/".format(folder_name))]
print(names)

for name in names:
    namesFile.write(name)
namesFile.close()

os.system("ffmpeg -f concat -safe 0 -i filenames.txt -c copy output.mp3" + " & timeout 15")


