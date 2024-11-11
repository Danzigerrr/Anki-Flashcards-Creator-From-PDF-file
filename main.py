from PDFFile import PDFFile
from pdf2image import convert_from_path
import os


def convert_pdf_file_to_images(pdf_file):
    images = convert_from_path(pdf_file.saving_dir + '/' + pdf_file.filename)

    saving_directory = 'images/' + pdf_file.filename.split('.')[0] + '/'

    # create directory if it does not exist
    if not os.path.exists(saving_directory):
        os.makedirs(saving_directory)

    # save each page as an JPEG image
    for i in range(len(images)):
        image_saving_dir = saving_directory + 'page' + str(i) + '.jpg'
        images[i].save(image_saving_dir, 'JPEG')
        pdf_file.images.append(image_saving_dir)


if __name__ == '__main__':
    dir_with_pdf = 'pdf_files'
    filename = 'part03-snlp.pdf'

    pdf_file = PDFFile(dir_with_pdf, filename)

    convert_pdf_file_to_images(pdf_file)

    print(f'Saved {len(pdf_file.images)} images in directory ')
