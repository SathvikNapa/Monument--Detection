import os
with open("labels.txt","w") as f:
	try:
		for i in os.listdir(os.getcwd()):
			f.write(i+"\n")
	except NotADirectoryError:
		print('ESCAPE')
