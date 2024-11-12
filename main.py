from PDFFile import PDFFile
from pdf2image import convert_from_path
import os
import PyPDF2
from flashcards_creator import define_model, create_notes, create_deck_with_notes, write_deck_to_file


def extract_images_from_pdf_file(pdf_file):
    images = convert_from_path(pdf_file.saving_dir + '/' + pdf_file.filename)

    saving_directory = pdf_file.get_images_path()

    # create directory if it does not exist
    if not os.path.exists(saving_directory):
        os.makedirs(saving_directory)

    # save each page as an JPEG image
    for i in range(len(images)):
        image_saving_dir = saving_directory + 'page' + str(i) + '.jpg'
        images[i].save(image_saving_dir, 'JPEG')
        pdf_file.images.append(image_saving_dir)

    print('Successfully converted each pdf page into an image')


def extract_text_from_pdf_file(pdf_file):
    with open(pdf_file.get_file_location(), 'rb') as file_to_convert:
        pdf_reader = PyPDF2.PdfReader(file_to_convert)

        # extract text from each page
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()
            pdf_file.text.append(text)

    print('Successfully extracted text from pdf file')


def extract_info_from_pdf():
    dir_with_pdf = 'pdf_files'
    filename = 'part02-nlp-1-10.pdf'

    pdf_file = PDFFile(dir_with_pdf, filename)

    extract_images_from_pdf_file(pdf_file)

    extract_text_from_pdf_file(pdf_file)

    print(pdf_file.get_content_head())

    return pdf_file


def create_flashcards(pdf_file: PDFFile):
    deck_name = pdf_file.get_filename_without_extension() + '_model'
    notes = create_notes(pdf_file)
    deck = create_deck_with_notes(notes, deck_name)
    write_deck_to_file(deck, deck_name, pdf_file)


if __name__ == '__main__':
    pdf_file = extract_info_from_pdf()
    create_flashcards(pdf_file)
