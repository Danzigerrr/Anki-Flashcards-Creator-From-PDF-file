from AnkiDeckReader import AnkiDeckReader

if __name__ == "__main__":
    filename = 'exported_decks/deck1.txt'
    deckReader = AnkiDeckReader(filename)
    deckReader.readFlashcards()
    deckReader.printFlashcards()









