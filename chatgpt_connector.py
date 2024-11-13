import openai
import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_APIKEY = os.getenv('OPENAI_APIKEY')
openai.api_key = OPENAI_APIKEY


def format_text(model_name, input_text):
    response = openai.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": "You are a text formatter that adds HTML tags to format text."},
            {"role": "user", "content": "Please format my text using only HTML tags. Make the key insight bold. "
                                        "Structure the text in an easy to follow way."},
            {"role": "user", "content": "Example input:\n\nFeature Representation\nFeature Engineering\n"
                                        "Importance of feature engineering\n• The features used determine the level "
                                        "of abstraction of o in x.\n• Some features generalize worse than others "
                                        "towards unseen data.\n• Engineering features that predict a target variable "
                                        "C and generalize well is key to effective feature-based NLP.\nFeature "
                                        "engineering in NLP\n• Standard features. Some types help in many tasks, "
                                        "e.g., bag-of-words.\n• Specific features. Often, the most discriminative "
                                        "types encode expert knowledge about the task and input.\nAlso, advanced "
                                        "versions of standard features exist, such as TF-IDF.\nFeature selection and "
                                        "dimensionality reduction\n• Techniques that aim to reduce the set of "
                                        "considered features to improve generalizability and training efficiency\n"
                                        "Not in the focus of this course"},
            {"role": "assistant", "content": "<h3>Feature Representation: Feature Engineering</h3><ul "
                                             "class=\"markdown-loose\"><li><b>Importance of Feature Engineering</b>:"
                                             "<ul class=\"markdown-tight\"><li>Determines {{c1::the <b>level of "
                                             "abstraction</b>}} for mapping inputs.</li><li>Some features <b>generalize "
                                             "better</b> on unseen data than others.</li><li>Designing features that "
                                             "<b>predict the target variable</b> and generalize well is essential for "
                                             "effective feature-based NLP.</li></ul></li><li><b>Feature Engineering in "
                                             "NLP</b>:<ul class=\"markdown-tight\"><li><b>{{c2::Standard}} features</b>: "
                                             "Common types, like <b>bag-of-words</b>, are helpful across various tasks."
                                             "</li><li><b>{{c3::Specific}} features</b>: Often encode <b>expert "
                                             "knowledge</b> and are highly discriminative for certain tasks.</li><li>"
                                             "<b>{{c4::Advanced}} versions</b> of standard features, like <b>TF-IDF</b>, "
                                             "can add more value.</li></ul></li><li><b>Feature Selection and "
                                             "Dimensionality Reduction</b>:<ul class=\"markdown-tight\"><li>Reduce the "
                                             "feature set to improve <b>generalizability</b> and <b>training "
                                             "efficiency</b>.</li></ul></li></ul>"},
            {"role": "user", "content": f"Now, please format the following text with HTML tags:\n\n{input_text}"}
        ]
    )
    formatted_text = response.choices[0].message.content

    return formatted_text


if __name__ == '__main__':
    model_name = "gpt-4o-mini"
    unformatted_text = """
        sample unformatted text
        """
    formatted_text = format_text(model_name, unformatted_text)
    print(formatted_text)
