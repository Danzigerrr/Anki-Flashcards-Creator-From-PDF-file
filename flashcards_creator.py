import genanki
import random


def generate_random_id():
    return random.randrange(1 << 30, 1 << 31)


def define_model(model_name):
    model_id = generate_random_id()
    my_model = genanki.Model(
        model_id,
        model_name,
        fields=[
            {'name': 'Question'},
            {'name': 'Answer'},
            {'name': 'Media'},
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '{{Question}}<br>{{Media}}',
                'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
            },
        ])

    return my_model


def create_deck(deck_name):
    deck_id = generate_random_id()
    deck = genanki.Deck(deck_id, deck_name)
    return deck


def create_notes(pdf_file):

    model = define_model("Basic Flashcards Model")

    notes = []

    q = "Question here {{c1:: qqqqq }}"
    a = "Answer here  {{c1:: aaaaa }} "
    m = "images/part02-nlp-1-10/page0.jpg"
    for i in range(2):
    # for i in range(len(pdf_file.images)):
        note = genanki.Note(
            model=genanki.CLOZE_MODEL,
            fields=[q, a])
        notes.append(note)
    return notes


def create_deck_with_notes(notes, deck_name):
    deck = create_deck(deck_name)

    for note in notes:
        deck.add_note(note)
    return deck


def write_deck_to_file(deck, filename, pdf_file):
    my_package = genanki.Package(deck)
    my_package.media_files = pdf_file.images  # ['sound.mp3', 'images/image.jpg']
    my_package.write_to_file(filename + '.apkg')

