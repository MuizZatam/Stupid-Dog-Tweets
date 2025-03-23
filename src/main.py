from modules.client import tweeter
from modules.gemini import generate_tweet


def main():

    client = tweeter()
    random_tweet = generate_tweet()

    client.create_tweet(text = random_tweet)


if __name__ == "__main__":

    main()