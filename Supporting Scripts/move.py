import os, subprocess
src = "/home/sathvik/Documents/ML_concepts/recognition"
dst = "/home/sathvik/Documents/ML_concepts/recognition/images"
listOfFiles = os.listdir(src)
for f in listOfFiles:
	try:
		for i in os.listdir(f):
			fullPath = src + "/" + f + "/" + i
			subprocess.Popen("mv" + " " + fullPath + " " + dst,shell=True)
	except NotADirectoryError:
		print('Not a directory Dude!')
