from pdf2image import convert_from_path
import os


def convert_pdf_file_to_images(dir_with_pdf, filename):
    images = convert_from_path(dir_with_pdf + '/' + filename)

    saving_directory = 'images/' + filename.split('.')[0] + '/'
    print(saving_directory)

    # create directory if it does not exist
    if not os.path.exists(saving_directory):
        os.makedirs(saving_directory)

    # convert each page into an image
    for i in range(len(images)):
        images[i].save(saving_directory + 'page' + str(i) + '.jpg', 'JPEG')

    print(f'Saved {len(images)} images in directory {saving_directory}')


if __name__ == '__main__':
    dir_with_pdf = 'pdf_files'
    filename = 'part03-snlp.pdf'
    convert_pdf_file_to_images(dir_with_pdf, filename)

