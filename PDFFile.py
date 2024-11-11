import json


class PDFFile:
    content = []

    def __init__(self, saving_dir, filename):
        self.saving_dir = saving_dir
        self.filename = filename

    def get_file_location(self):
        return self.saving_dir + '/' + self.filename

    def get_filename_without_extension(self):
        return self.filename.split('.')[0] + '/'

    def get_images_path(self):
        return 'images/' + self.get_filename_without_extension()

    def get_content_head(self):
        return f"Content:\n{json.dumps(self.content[:5], indent=4)}"


