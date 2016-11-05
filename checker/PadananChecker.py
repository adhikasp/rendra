from checker.BaseChecker import *
import os.path
import re

class PadananChecker(BaseChecker):
    def __init__(self, dictionary = None):
        super().__init__("Padanan Kata Checker")
        self.dictionary = {}
        self.dictionary_key = []
        self.prepared = False

        if (self.dictionary != None):
            self.prepareDict(dictionary)

    def prepareDict(self, path):
        if (not(os.path.exists(path))):
            print("File {} doesn't exist.".format(path))
            return

        for element in open(path).readlines():
            element = element.split("|")
            self.dictionary[element[0]] = element[1].strip("\n").split(";")
            self.dictionary_key.append(element[0])

        self.prepared = True

    def check(self, source, translation):
        if (not(self.prepared)):
            print("The dictionary is not prepared.")
            return []

        errList = []

        for term in self.dictionary:

            # this is SLOW but do the job
            regex_term = r"\b" + term + r"\b"
            if (re.search(regex_term, translation)):
                error_message = ErrorMessage(
                                             self,
                                             source,
                                             translation,
                                             "The possible translation for '{}'' is {}".format(term, self.dictionary[term]))
                errList.append(error_message)

        return errList
