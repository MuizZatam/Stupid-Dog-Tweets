from modules.client import tweeter
from modules.respond import respond_to_mentions
from modules.gemini import generate_tweet


def main():

    client = tweeter()
    random_tweet = generate_tweet()

    client.create_tweet(text = random_tweet)

    respond_to_mentions()

    

if __name__ == "__main__":

    main()