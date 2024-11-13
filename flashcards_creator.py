import genanki
import random
import os
from genanki import Model

from chatgpt_connector import format_text_as_html


def generate_random_id():
    return random.randrange(1 << 30, 1 << 31)


def define_model(model_name):
    model_id = generate_random_id()
    my_model = genanki.Model(
        model_id,
        model_name,
        model_type=Model.CLOZE,
        fields=[
            {
                'name': 'Text',
                'font': 'Arial',
            },
            {
                'name': 'Back Extra',
                'font': 'Arial',
            },
            {
                'name': 'MyMedia',
                'font': 'Arial',
            },
        ],
        templates=[
            {
                'name': 'Cloze',
                'qfmt': '{{cloze:Text}}',
                'afmt': '{{cloze:Text}}<br>\n{{Back Extra}} <br>{{MyMedia}}',
            },
        ],
        css='.card {\n font-family: arial;\n font-size: 20px;\n text-align: center;\n color: black;\n background-color: white;\n}\n\n'
            '.cloze {\n font-weight: bold;\n color: blue;\n}\n.nightMode .cloze {\n color: lightblue;\n}',
    )

    return my_model


def create_deck(deck_name):
    deck_id = generate_random_id()
    deck = genanki.Deck(deck_id, deck_name)
    return deck


def create_notes(pdf_file):
    model = define_model("Cloze Flashcards Model - python project")

    notes = []

    # Loop over each page of the PDF
    for i in range(len(pdf_file.text)):
        # Extract the text for the current page
        page_text = pdf_file.text[i]

        # Check if the page text is longer than 10 words
        if len(page_text.split()) > 10:
            # Format the page text using OpenAI API (you may adjust this further for your needs)
            formatted_text = format_text_as_html(page_text)
        else:
            # If the text is not longer than 10 words, just use it as-is
            formatted_text = page_text

        # Image filename corresponding to the page
        image_filename = pdf_file.get_filename_without_extension() + f"_page{i}.jpg"

        # Constructing the HTML structure (you can modify this structure as needed)
        q = formatted_text
        a = f'<br>Page: {i + 1} <br> <img src="{image_filename}">'  # Image for the current page
        m = f"<br><br>"  # This can be adjusted based on your needs (answer part)

        # Create a note for the page
        note = genanki.Note(
            model=model,
            fields=[q, a, m]
        )

        notes.append(note)

    return notes


def create_deck_with_notes(notes, deck_name):
    deck = create_deck(deck_name)

    for note in notes:
        deck.add_note(note)
    return deck


def write_deck_to_file(deck, filename, pdf_file):
    my_package = genanki.Package(deck)
    my_package.media_files = pdf_file.images

    saving_directory = "generated_decks/"

    # create directory if it does not exist
    if not os.path.exists(saving_directory):
        os.makedirs(saving_directory)

    my_package.write_to_file(saving_directory + filename + '.apkg')
