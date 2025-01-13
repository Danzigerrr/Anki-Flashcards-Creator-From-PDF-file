import genanki
import random
import os
from genanki import Model
from FlashcardsCreator import FlashcardsCreator


class AnkiDeckCreator:
    generated_flashcards = []

    def __init__(self, flashcardsCreator):
        self.flashcardsCreator = flashcardsCreator

    def generate_random_id(self):
        return random.randrange(1 << 30, 1 << 31)

    def define_model(self, model_name):
        model_id = self.generate_random_id()
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
                    'qfmt': '''
                        <div class="note">
                            <div class="front k">
                                <div class="question row">
                                   {{cloze:Text}}
                                </div>
                            </div>
                        </div>
                    ''',
                    'afmt': '''
                        <div class="note">
                            <div class="front k">
                                <div class="row">
                                    {{cloze:Text}}
                                    <br>
                                    {{Back Extra}}
                                </div>
                            </div>
                        </div>
                    ''',
                },
            ],
            css='''
                .card {
                 font-family: arial;
                 font-size: 20px;
                 text-align: center;
                 color: black;
                 background-color: white;
                }
                
                .cloze {
                 font-weight: bold;
                 color: lightblue;
                }
                
                /* BODY */
                html, body {
                    background-color: dark !important;
                    margin: 0 !important;
                    padding: 0;
                    height: 100%;
                    width: 100%;
                    max-height: 100vh;
                    max-width: 100vw;
                    font-family: San Francisco, "Noto Sans KR", Helvetica, Arial;
                    font-weight: 400;
                    font-size: 18px;
                    word-break: keep-all;
                    text-align: left;
                    overflow: auto;    
                }
                
                /* CARD */
                
                .row {
                    padding-left: 15%;
                    padding-right: 15%;
                    padding-top: 2%;
                }
            ''',
        )

        return my_model


    def create_deck(self, deck_name):
        deck_id = self.generate_random_id()
        deck = genanki.Deck(deck_id, deck_name)
        return deck



    def create_notes(self, flashcardsCreator: FlashcardsCreator):
        model = self.define_model("Cloze Flashcards Model - python project")
        notes = []

        for flashcard in flashcardsCreator.flashcards:
            notes.append(self.flashcardsCreator.transform_content_into_flashcard(flashcard, model))

        return notes


    def create_deck_with_notes(self, notes, deck_name):
        deck = self.create_deck(deck_name)

        for note in notes:
            deck.add_note(note)
        return deck


    def write_deck_to_file(self, deck, filename):
        my_package = genanki.Package(deck)

        saving_directory = "generated_decks_questions/"

        # create directory if it does not exist
        if not os.path.exists(saving_directory):
            os.makedirs(saving_directory)

        my_package.write_to_file(saving_directory + filename + '.apkg')
