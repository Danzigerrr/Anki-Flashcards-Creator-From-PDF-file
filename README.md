# Create Anki Flashcards from PDF using ChatGPT


## How to use

First save your input pdf file into the `pdf_files` directory.
Then, run the `main.py` file.
Finally, the resulting `*.akpg` file will appear in `generated_decks` directory with the same filename as your input pdf file.

In the root directory create an `.env` file where you store your OPEN API key (keep it secret):
```
OPENAI_APIKEY=insert_your_API_key_here
```

## Installation

The `requirements.txt` file was created using pipreqs library. The following command:
```bash
pipreqs . --ignore ".venv" 
```

In order to install the libraries use the following command: (if you don't already have virtualenv installed)
```bash
pip install virtualenv 
```


Create your new environment (called 'venv' here):
```bash
virtualenv venv
```

Activate the virtual environment: (unix/linux)
```bash
source venv/bin/activate # linux
```

Install the requirements in the current environment:
```bash
pip install -r requirements.txt 
```


## License
MIT

## Contributions
Are welcome!