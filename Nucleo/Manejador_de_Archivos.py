# -*- coding:utf-8 -*-

class FileManager:
    
    def __init__(self):
        pass

    def readFile(self, fileName):
        try:
            f = open(fileName, "r")
            content = f.read()
            f.close()
            return content
        
        except:
            pass

    def createFile(self, fileName, content):
        f = open(fileName, "w")
        f.write(content)
        f.close()

    