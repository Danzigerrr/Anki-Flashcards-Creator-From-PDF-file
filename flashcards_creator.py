import genanki
import random
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
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


def create_deck(deck_name):
    deck_id = generate_random_id()
    deck = genanki.Deck(deck_id, deck_name)
    return deck


def process_page(i, page_text, pdf_file, model, words_limit=15):
    """Process a single page to generate a note."""
    if len(page_text.split()) > words_limit:
        # Format the page text using OpenAI API (you may adjust this further for your needs)
        formatted_text = format_text_as_html(page_text, pdf_file.get_topic(), pdf_file.get_notes())
    else:
        # If the text is not longer than words_limit words, just use it as-is
        formatted_text = page_text + " {{c1::todo}}"
        print(f"\nPage: {i}; formatted_text shorter than {words_limit} words\n")

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

    return i, note


def create_notes(pdf_file):
    model = define_model("Cloze Flashcards Model - python project")
    notes = []
    words_limit = 15

    # Use ThreadPoolExecutor for parallel processing
    with ThreadPoolExecutor() as executor:
        futures = {
            executor.submit(process_page, i, pdf_file.text[i], pdf_file, model, words_limit): i
            for i in range(len(pdf_file.text))
        }

        # Initialize the progress bar
        for future in tqdm(as_completed(futures), total=len(futures), desc="Processing Pages with OpenAI Model", unit="page"):
            i, note = future.result()  # Unpack the page index and generated note
            notes.append((i, note))

    # Sort the notes by page number to ensure alignment
    sorted_notes = [note for _, note in sorted(notes, key=lambda x: x[0])]

    return sorted_notes


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
