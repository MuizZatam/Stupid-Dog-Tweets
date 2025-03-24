from dotenv import load_dotenv
import os
import google.generativeai as genai


load_dotenv()
GEMINI_KEY = os.environ.get('GEMINI_KEY')
genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")


def generate_tweet():

    response = model.generate_content("Generate a short, philosophical one-liner inspired by *Courage the Cowardly Dog*, referencing themes of fear, courage, and the unknown—optionally including a direct quote, easter egg from the show, dialogues, or a poetic touch (under 200 characters).")

    return response.text


if __name__ == "__main__":

    print(generate_tweet())