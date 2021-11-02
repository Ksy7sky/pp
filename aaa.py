from os import walk
import urllib.parse, urllib.request, urllib.error
import re

#set
mypath = "/run/media/mw/data2/youtube/pdp/2017/"
fileName = "/run/media/mw/data2/youtube/pdp/2017/2017"
extentions = ["webm", "mkv", "mp4"]

#dynamic
folderFileList = []
fileFileList = []
out = []







def saveToFile(l: list):
    textfile = open("to_download.txt", "w")
    for element in l:
        textfile.write(element + "\n")
    textfile.close()


def getName(url: str) -> str:
    name = ""
    pos = re.search('[0-9]+_', url)
    if pos != None:
        name = url[pos.regs[0][1]:]
        return name
    return name


def formatURL(url: str) -> str:
    name = url + getName(url)[:-1]
    return name


def getFinalURL(line: str) -> str:
    for ext in extentions:
        finalURL = formatURL(line) + '.' + ext
        try: urllib.request.urlopen(finalURL)
        except urllib.error.HTTPError as e:continue
        except urllib.error.URLError as e:continue
        else:return finalURL
    return 'error ' + line


# def download(url: str):
#     urllib.request.urlretrieve(url)







for (dirpath, dirnames, filenames) in walk(mypath):
    folderFileList += filenames

# remove extention from filenames
for string in folderFileList:
    st = string[:string.rfind('.')]
    id = folderFileList.index(string)
    folderFileList[id] = st

with open(fileName) as file:
    for line in file:
        fileFileList += [line.strip()]

# remove existing
for line in folderFileList:
    for word in fileFileList:
        if line == urllib.parse.unquote(getName(word)[:-1]):
            fileFileList.pop(fileFileList.index(word))


# make final list
anotherOne = []
for url in fileFileList:
    anotherOne += [getFinalURL(url)]



saveToFile()