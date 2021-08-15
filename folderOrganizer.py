#!/usr/bin/python
# or call '$ which python' to get the correct path

# Steps to make this program executable from the command line:
# don't forget to make this file executable with 'chmod +x ./fileOrganizer.py'
# sudo cp ./fileOrganizer.py /usr/local/bin/forg
# call $ forg in any dir you want to clean except for critical ones such as Home and other places


# TODO:
# - add multiple paths as arguments
# - prompt user to overrite existing files or rename them


import os

def getCleanDir(format: str) -> str:
    dir = "Unknown"

    if format == "":
        dir = "Unknown"  # do nothing
    elif format in documentsList:
        dir = "Documents"
    elif format in imagesList:
        dir = "Images"
    elif format in videosList:
        dir = "Videos"
    elif format in archivesList:
        dir = "Archives"
    elif format in srcList:
        dir = "SRC files"
    elif format in audioList:
        dir = "Audio"
    elif format in CADList:
        dir = "CAD files"

    return cwd+"/"+dir

documentsList = ['.pdf', '.txt', '.odt', '.docs', '.docx', '.ods', '.xls', '.xlsx', '.xls', '.csv', '.odp', '.ppt', '.pps', '.ppsx', '.pptx', '.pptm']
srcList       = ['.c', '.cpp', '.h', '.o', '.so','.a', '.bin', '.hex', '.s', '.asm', '.java', '.xml', '.html', '.py']
CADList       = ['.stl', '.FCStd', '.FCMacro', '.cam', '.max','.obj','.step','.scad', '.3ds', 'stp', '.blend' ]
archivesList  = ['.zip', '.7z', '.rar', '.gz', '.iso', '.img', '.bz2', '.bz', '.tar']
audioList     = ['.mp3', '.wav', 'aac', 'm4a', 'mpa', 'wma']
videosList    = ['.mp4', '.mkv', '.mpeg', '.mpg', '.webm']
imagesList    = ['.jpg', '.jpeg', '.png', '.svg', '.ai']
 
cwd = os.getcwd()
filesList = os.listdir()

for f in filesList:
    filePath = cwd+'/'+f

    # skip if its the script's fime
    if f == "folderOrganizer.py":
        continue

    # check if not a directory
    if(os.path.isfile(filePath)): 
        fileFormat = os.path.splitext(filePath)[1]
        cleanDir= getCleanDir(fileFormat)
        try:
            # create appropriate folder if not available
            if not os.path.exists(cleanDir):
                os.mkdir(cleanDir)
            # Move the file to appopriate folder
            os.replace(filePath, cleanDir+'/'+f)
            print(f+' is successfuly moved to: ' + cleanDir)
        except:
            print('moving '+f+' to: ' + cleanDir + " failed :( ,try to run the program as root!")


