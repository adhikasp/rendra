class BaseChecker:
    def __init__(self, desc):
        self.checkerDescription = desc;

    def check(self, source, translation):
        print("Method 'check' not implemented")

class ErrorMessage:
    def __init__(self, checker, source, translation, message):
        self.checkerDescription = checker.checkerDescription
        self.source = source
        self.translation = translation
        self.message = message

    def show(self):
        print("Checker           : {}".format(self.checkerDescription))
        print("Source text       : {}".format(self.source))
        print("Translation text  : {}".format(self.translation))
        print("Message           : {}".format(self.message))
        print()
