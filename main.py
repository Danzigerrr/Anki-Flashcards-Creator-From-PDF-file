from PDFFile import PDFFile
from pdf2image import convert_from_path
import os
import PyPDF2


def extract_images_from_pdf_file(pdf_file):
    images = convert_from_path(pdf_file.saving_dir + '/' + pdf_file.filename)

    saving_directory = 'images/' + pdf_file.get_filename_without_extension()

    # create directory if it does not exist
    if not os.path.exists(saving_directory):
        os.makedirs(saving_directory)

    # save each page as an JPEG image
    for i in range(len(images)):
        image_saving_dir = saving_directory + 'page' + str(i) + '.jpg'
        images[i].save(image_saving_dir, 'JPEG')
        pdf_file.content.append({'image': image_saving_dir})

    print('Successfully converted each pdf page into an image')


def extract_text_from_pdf_file(pdf_file):
    with open(pdf_file.get_file_location(), 'rb') as file_to_convert:
        pdf_reader = PyPDF2.PdfReader(file_to_convert)

        # extract text from each page
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()
            pdf_file.content[page_num].update({'text': text})

    print('Successfully extracted text from pdf file')


if __name__ == '__main__':
    dir_with_pdf = 'pdf_files'
    filename = 'part02-nlp-1-10.pdf'

    pdf_file = PDFFile(dir_with_pdf, filename)

    extract_images_from_pdf_file(pdf_file)

    extract_text_from_pdf_file(pdf_file)
