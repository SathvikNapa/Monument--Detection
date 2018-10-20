'''import os
import sys

top_dir = os.path.abspath('/home/sathvik/Documents/ML_concepts/recognition/Abu Simbel in Egypt')
files = os.listdir( top_dir )

for index,item in enumerate(files):
    if os.path.isdir( os.path.join(top_dir,item) ):
       files.pop(index)

files.sort()

duplicates = []
last_index = None
for index,item in enumerate(files):

    last_index = index
    extension = ""
    if '.' in item:
        extension = '.' + item.split('.')[-1]
    old_file = os.path.join(top_dir,item)
    new_file = os.path.join(top_dir,str(index) + extension  )
    while os.path.isfile(new_file):
          last_index += 1
          new_file = os.path.join(top_dir,str(last_index) + extension  )
    print( old_file + ' renamed to ' + new_file ) 
    os.rename(old_file,new_file)
'''
import os
 
# Function to rename multiple files
def main():
    i = 0
     
    for files in os.listdir(os.getcwd()):
        for filename in os.listdir(os.getcwd()):
            dst =filename + str(i) + ".jpg"
            src =os.getcwd()+'/'+ filename
            dst =os.getcwd()+'/'+ dst
         
        # rename() function will
        # rename all the files
            os.rename(src, dst)
            i += 1
 
# Driver Code
if __name__ == '__main__':
     
    # Calling main() function
    main()
