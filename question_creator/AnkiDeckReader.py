from pathlib import Path
import re


class AnkiDeckReader:
    flashcards = []

    def __init__(self, filename):
        self.filename = filename

    def readFlashcards(self):
        file_content = self.read_exported_deck()
        self.flashcards = self.read_every_flashcard(file_content)

    def printFlashcards(self):
        print("Flashcards content:")
        for flashcard in self.flashcards:
            print(flashcard)

    def remove_anki_cloze_deletions_brackets(self, input_text):
        return re.sub(r"\{\{c\d+::(.*?)\}\}", r"\1", input_text)

    def remove_html_tags(self, input_text):
        return re.sub(r"<.*?>", " ", input_text)

    def read_exported_deck(self):
        return Path(self.filename).read_text(encoding='utf-8')

    def read_every_flashcard(self, file_content):
        flashcards = []
        lines = file_content.split('\n')[4:]
        for line in lines:
            if line.strip():  # Skip empty lines
                content = line.split("\t")[2]  # Get the third element
                content_without_cloze_brackets = self.remove_anki_cloze_deletions_brackets(content)
                cleaned_text = self.remove_html_tags(content_without_cloze_brackets)
                flashcards.append(cleaned_text)
        return flashcards

