class PDFFile:
    images = []

    def __init__(self, saving_dir, filename):
        self.saving_dir = saving_dir
        self.filename = filename

    def myfunc(self):
        print("Hello my name is " + self.name)