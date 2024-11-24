import openai
import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_APIKEY = os.getenv('OPENAI_APIKEY')
openai.api_key = OPENAI_APIKEY


def format_text_as_html(input_text, pdf_file_topic, lecture_notes, model_name="gpt-4o-mini"):
    response = openai.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": "You are a text formatter that adds HTML tags to format text with key "
                                          "insights bolded."
                                          "The text comes from lecture slides on the topic of: " + pdf_file_topic +
                                          "The response should end with empty Anki cloze deletion brackets:"
                                          " {{c1::todo}}. "
                                          "Adjust the wording slightly to improve readability - use simple language. "
                                          "You can change the content of the text for better understanding - "
                                          "especially write things more concisely and in a shorter form. "
                                          "Ensure key knowledge points are highlighted(bold) "
                                          "and clearly structured."
                                          "Use British English in your response."
                                          "Ignore any irrelevant information such as lecture name, page number, "
                                          "author of slides, etc."
                                          "Write your answer in a concise way making clear the key insights from the "
                                          "pdf page of the lecture file."
                                          "Please write shortly - compress the knowledge "
                                          "to only include the key insights!"
                                          "You can also add some simple explanation of the "
                                          "content presented in this lecture slide."},
            {"role": "user", "content": "Please format my text using HTML tags. Make key insights bold, "
                                        "and add {{c1::todo}} at the end of the response."},
            {
                "role": "user",
                "content": "Natural Language Processing\n\nNLP is a field of AI focused on the interaction between "
                           "computers and human language. It involves applications like machine translation, "
                           "text summarization, and sentiment analysis."
            },
            {
                "role": "assistant",
                "content": "<h3>Natural Language Processing (NLP)</h3><ul><li><b>NLP</b> bridges <b>human "
                           "language</b> and <b>computers</b>, enabling machines to understand and process text or "
                           "speech.</li><li>Key applications: <b>translation</b> between languages, "
                           "creating <b>summaries</b> of long texts, and identifying <b>emotions</b> in "
                           "text.</li></ul>{{c1::todo}}"
            },
            {"role": "user", "content": f"My personal notes on this topic:\n\n{lecture_notes}. "
                                        f"Please use them during generating the text describing "
                                        f"the content presented in this lecture."},
            {"role": "user", "content": f"Now, please format the following text with HTML tags:\n\n{input_text}"}
        ]
    )

    formatted_text = response.choices[0].message.content

    return formatted_text


