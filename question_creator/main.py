from pathlib import Path
import re


def remove_anki_cloze_deletions_brackets(input_text):
    return re.sub(r"\{\{c\d+::(.*?)\}\}", r"\1", input_text)


def remove_html_tags(input_text):
    return re.sub(r"<.*?>", " ", input_text)


def read_exported_deck(filename):
    return Path(filename).read_text(encoding='utf-8')


def read_every_flashcard(file_content):
    flashcards = []

    lines = file_content.split('\n')[4:]
    for line in lines:
        if line.strip():  # Skip empty lines
            content = line.split("\t")[2]  # Get the third element
            content_without_cloze_brackets = remove_anki_cloze_deletions_brackets(content)
            cleaned_text = remove_html_tags(content_without_cloze_brackets)
            flashcards.append(cleaned_text)

    return flashcards


if __name__ == "__main__":
    filename = 'exported_decks/deck1.txt'
    file_content = read_exported_deck(filename)
    flashcards = read_every_flashcard(file_content)
    print(flashcards)

