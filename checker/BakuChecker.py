from checker.BaseChecker import *
import os.path

class BakuChecker(BaseChecker):
    def __init__(self, dict = None):
        super().__init__("Kata Baku Checker")
        self.dict = []
        self.prepared = False

        if (dict != None):
            self.prepareDict(dict)

    def prepareDict(self, path):
        if (not(os.path.exists(path))):
            print("File {} doesn't exist.".format(path))
            return

        for element in open(path).readlines():
            element = element.split("|")
            element[0] = element[0].strip()
            element[1] = element[1].strip()
            
            self.dict.append(element)

        self.prepared = True

    def slice(self, text, start, length, helperLength = 20):
        ret = ""
        ed = ""

        if (start>helperLength):
            ret += "..."
            st = start-helperLength
        else:
            st = 0

        if (start+length+helperLength < len(text)):
            ed += "..."
            end = start+length+helperLength
        else:
            end = len(text)

        return ret+text[st:end]+ed

    def check(self, text):
        if (not(self.prepared)):
            print("The dictionary is not prepared.")
            return []

        errList = []

        textLower = text.lower()

        for element in self.dict:
            i = 0

            while(textLower.find(element[1], i)!=-1):
                i = textLower.find(element[1], i)
                errList.append(ErrorMessage(self, self.slice(text, i, len(element[1])), "The correct word for '{}' is '{}'".format(element[1], element[0])))

                i += len(element[1])

        return errList
