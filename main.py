from PDFFile import PDFFile
from flashcards_creator import create_notes, create_deck_with_notes, write_deck_to_file


def extract_info_from_pdf():
    dir_with_pdf = 'pdf_files'
    filename = 'examplefile.pdf'

    pdf_file = PDFFile(dir_with_pdf, filename)

    pdf_file.extract_images_from_pdf_file()

    pdf_file.extract_text_from_pdf_file()

    print(pdf_file.get_content_head())

    return pdf_file


def create_flashcards(input_pdf_file: PDFFile):
    deck_name = input_pdf_file.get_filename_without_extension()
    notes = create_notes(input_pdf_file)
    deck = create_deck_with_notes(notes, deck_name + '_model')
    write_deck_to_file(deck, deck_name, input_pdf_file)


if __name__ == '__main__':
    pdf_file = extract_info_from_pdf()
    create_flashcards(pdf_file)
