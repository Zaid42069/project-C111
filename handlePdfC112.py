import os
import shutil
fromDir="C:/Users/imran/Downloads"
toDir="D:/codeFileWhj"
listOfFiles=os.listdir(fromDir)
print(listOfFiles)

for fileName in listOfFiles:
    name,extension= os.path.splitext(fileName)
    print(name)
    print(extension)
    if extension=="":
       continue
    if extension in [".pdf"]:
        path1=fromDir+"/"+fileName
        path2=toDir+'/'+"pdfs"
        path3=toDir+'/'+"pdfs"+"/"+fileName
        print("path1 = ",path1)
        print("path3 = ",path3)

        if os.path.exists(path2):
            print("Moving...."+fileName+"---")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("Moving...."+fileName+"---")
            shutil.move(path1,path3)
