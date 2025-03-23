from dotenv import load_dotenv
import os
import google.generativeai as genai
from random import choice


load_dotenv()
GEMINI_KEY = os.environ.get('GEMINI_KEY')
genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")


def generate_tweet_prompt():

    prompts = [
        "Generate a philosophical quote inspired by Courage the Cowardly Dog that's exactly one sentence long. Make it thoughtful and simple. Without any twitter hashtags, markdown formatting and in one line.",
        "Create a short philosophical thought (under 200 characters) that Courage The Cowardly Dog might think while facing his fears. Without any twitter hashtags, markdown formatting and in one line.",
        "Write a brief existential observation that references the theme of courage despite fear. Keep it under 200 characters. Without any twitter hashtags, markdown formatting and in one line.",
        "Generate a philosophical one-liner about finding courage in a scary world, inspired by the show Courage the Cowardly Dog. Without any twitter hashtags, markdown formatting and in one line.",
        "Write a short, philosophical tweet that subtly references 'Nowhere' from Courage The Cowardly Dog as both a place and a metaphorical concept. Without any twitter hashtags, markdown formatting and in one line.",
        "Generate a short tweet directly referencing quotes and easter eggs from the show - Courage the Cowardly Dog"
    ]

    return choice(prompts)


def generate_tweet():

    prompt = generate_tweet_prompt()
    response = model.generate_content(prompt)

    return response.text


if __name__ == "__main__":

    print(generate_tweet())