from datetime import datetime
files = ['file1.txt','file2.txt','file3.txt']
filename = str(datetime.now())+".txt"
print(filename)
with open(filename,'a') as fmerge:
    for file in files:
        with open(file, 'r') as f:
            content = f.read()
            fmerge.write(content + "\n")
