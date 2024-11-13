import genanki
import random
import os
from genanki import Model


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
                'name': 'Text'
            },
            {
                'name': 'Back Extra'
            },
            {
                'name': 'MyMedia'
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

    model = define_model("Cloze aaa Flashcards Model")

    notes = []

    # HTML encoding
    q = "<div><strong>Distributed Systems Challenges:</strong></div><ul><li>Machines act {{c1::independently}}, communicating only via {{c2::a network}}</li></ul>"
    a = "<br>Back extra here"
    # image must have a unique filename
    image_filename = pdf_file.get_filename_without_extension() + "_page0.jpg"
    m = f'<img src="{image_filename}">'

    for i in range(2):
    # for i in range(len(pdf_file.images)):
        note = genanki.Note(
            model=model,
            fields=[q, a, m])
        notes.append(note)
    return notes


def create_deck_with_notes(notes, deck_name):
    deck = create_deck(deck_name)

    for note in notes:
        deck.add_note(note)
    return deck


def write_deck_to_file(deck, filename, pdf_file):
    my_package = genanki.Package(deck)
    my_package.media_files = ['images/part02-nlp-1-10/part02-nlp-1-10_page0.jpg']

    saving_directory = "generated_decks/"

    # create directory if it does not exist
    if not os.path.exists(saving_directory):
        os.makedirs(saving_directory)

    my_package.write_to_file(saving_directory + filename + '.apkg')

