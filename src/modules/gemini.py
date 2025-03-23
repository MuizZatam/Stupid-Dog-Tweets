from dotenv import load_dotenv
import os
import google.generativeai as genai
from random import choice


load_dotenv()
GEMINI_KEY = os.environ.get('GEMINI_KEY')
genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel("gemini-1.5-flash-8b")


def generate_tweet_prompt():

    prompts = [
        "Generate a philosophical quote inspired by Courage the Cowardly Dog that's exactly one sentence long. Make it thoughtful and simple. Without any twitter hashtags, markdown formatting and in one line.",
        "Create a short philosophical thought (under 200 characters) that Courage The Cowardly Dog might think while facing his fears. Without any twitter hashtags, markdown formatting and in one line.",
        "Write a brief existential observation that references the theme of courage despite fear. Keep it under 200 characters. Without any twitter hashtags, markdown formatting and in one line.",
        "Generate a philosophical one-liner about finding courage in a scary world, inspired by the show Courage the Cowardly Dog. Without any twitter hashtags, markdown formatting and in one line.",
        "Write a short, philosophical tweet that subtly references 'Nowhere' from Courage The Cowardly Dog as both a place and a metaphorical concept. Without any twitter hashtags, markdown formatting and in one line.",
        "Generate a short tweet directly referencing quotes and easter eggs from the show - Courage the Cowardly Dog. Without any twitter hashtags, markdown formatting and in one line.",
        "Quote a random saying/quote from Courage the Cowardly Dog.  Without any twitter hashtags, markdown formatting and in one line.",
        "Say a random poem/sonnet (under 200 characters) and also quote the author .Without any twitter hashtags, markdown formatting and in one line."
    ]

    return choice(prompts)


def generate_tweet():

    prompt = generate_tweet_prompt()
    response = model.generate_content(prompt)

    return response.text


def generate_response(mention):

    prompt = f"You are Courge The Dog - A Twitter Bot talking about Philosophy with references to the show itself. Respond to the following: '{mention}' in a simple, plain and a humorous way while referencing the show and it's easter eggs. Please use no markdown formatting, keep it all on one line and add no hashtags or anything alike."

    response = model.generate_content(prompt)

    return response.text


if __name__ == "__main__":

    print(generate_tweet())