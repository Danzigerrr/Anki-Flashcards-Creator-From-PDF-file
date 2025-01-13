import genanki
import openai
import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_APIKEY = os.getenv('OPENAI_APIKEY')
openai.api_key = OPENAI_APIKEY


class FlashcardsCreator:
    flashcards = []

    def __init__(self, deckReader):
        self.deckReader = deckReader

    def transform_content_into_flashcard(self, content, ankiModel):
        """Process a single page to generate a note."""
        # Format the page text using OpenAI API (you may adjust this further for your needs)
        flashcard = self.create_questions_with_ai_model(content)

        # Constructing the HTML structure (you can modify this structure as needed)
        q = flashcard
        a = f"<br><br>"  # Image for the current page
        m = f"<br><br>"  # This can be adjusted based on your needs (answer part)

        # Create a note for the page
        note = genanki.Note(
            model=ankiModel,
            fields=[q, a, m]
        )

        return note


    def create_questions_with_ai_model(self, input_text, pdf_file_topic, lecture_notes, model_name="gpt-4o-mini"):
        response = openai.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": ""},
                {"role": "user", "content": "Please create questions which will examine my knowlege on the presented content. "
                                            "The answer to the questions together with justification for this answer "
                                            "should be given in the folloing format: {{c1::answer, justiication}}. "},
                {
                    "role": "user",
                    "content": "Example content of the imported flashcards"
                },
                {
                    "role": "assistant",
                    "content": "Example Question or Questions"
                               "{{c1::Example Answer with Explanation}}"
                },
            ]
        )

        formatted_text = response.choices[0].message.content

        return formatted_text




