class PDFFile:
    content = []

    def __init__(self, saving_dir, filename):
        self.saving_dir = saving_dir
        self.filename = filename

    def get_file_location(self):
        return self.saving_dir + '/' + self.filename

    def get_filename_without_extension(self):
        return self.filename.split('.')[0] + '/'


