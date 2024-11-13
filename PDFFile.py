import json
from pdf2image import convert_from_path
import os
import PyPDF2


class PDFFile:
    filename = ""
    saving_dir = ""
    images = []
    text = []

    def __init__(self, saving_dir, filename):
        self.saving_dir = saving_dir
        self.filename = filename

    def get_file_location(self):
        return self.saving_dir + '/' + self.filename

    def get_filename_without_extension(self):
        return self.filename.split('.')[0]

    def get_images_path(self):
        return 'images/' + self.get_filename_without_extension()

    def get_content_head(self):
        return f"Content:\n{json.dumps(self.text[:5], indent=4)}"

    def get_filename(self):
        return self.filename

    def get_saving_dir(self):
        return self.saving_dir

    def extract_images_from_pdf_file(self):
        images = convert_from_path(self.saving_dir + '/' + self.filename)

        saving_directory = self.get_images_path()

        # create directory if it does not exist
        if not os.path.exists(saving_directory):
            os.makedirs(saving_directory)

        # save each page as an JPEG image
        for i in range(len(images)):
            image_saving_dir = saving_directory + '/' + self.get_filename_without_extension() + '_page' + str(
                i) + '.jpg'
            images[i].save(image_saving_dir, 'JPEG')
            self.images.append(image_saving_dir)

        print('Successfully converted each pdf page into an image')

    def extract_text_from_pdf_file(self):
        with open(self.get_file_location(), 'rb') as file_to_convert:
            pdf_reader = PyPDF2.PdfReader(file_to_convert)

            # extract text from each page
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
                self.text.append(text)

        print('Successfully extracted text from pdf file')
