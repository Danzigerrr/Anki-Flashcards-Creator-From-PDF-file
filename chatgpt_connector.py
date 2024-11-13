import openai
import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_APIKEY = os.getenv('OPENAI_APIKEY')
openai.api_key = OPENAI_APIKEY


def format_text_as_html(input_text, model_name="gpt-4o-mini"):
    response = openai.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": "You are a text formatter that adds HTML tags to format text with key "
                                          "insights bolded."
                                          "The response should end with empty Anki cloze deletion brackets:"
                                          " {{c1::todo}}. "
                                          "You may adjust the wording slightly to improve readability. "
                                          "Ensure key knowledge points are highlighted "
                                          "and clearly structured."},
            {"role": "user", "content": "Please format my text using HTML tags. Make key insights bold, "
                                        "and add {{c1::todo}} at the end of the response."},
            {"role": "user", "content": "Example input:\n\nNatural Language Processing\n\nNLP "
                                        "is a field of AI focused on the interaction between "
                                        "computers and human language. It involves applications "
                                        "like machine translation, text summarization, "
                                        "and sentiment analysis."},
            {"role": "assistant", "content": "<h3>Natural Language Processing (NLP)</h3><ul><li>NLP"
                                             " is a field of AI focused on "
                                             "the <b>interaction between computers and human "
                                             "language</b>.</li><li>It involves applications "
                                             "such as <b>machine translation</b>, <b>text summarization</b>,"
                                             " and <b>sentiment analysis</b>.</li></ul>"
                                             "{{c1::todo}}"},
            {"role": "user", "content": f"Now, please format the following text with HTML tags:\n\n{input_text}"}
        ]
    )

    formatted_text = response.choices[0].message.content

    return formatted_text


if __name__ == '__main__':
    unformatted_text = """
        sample unformatted text
        """
    formatted_text = format_text_as_html(unformatted_text)
    print(formatted_text)
