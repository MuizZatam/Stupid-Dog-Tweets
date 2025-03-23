from .gemini import generate_response
from .client import tweeter
import os


try:
    responder = tweeter()
    bot_user = responder.get_me()
    bot_id = bot_user.data.id
    print(f"Bot ID: {bot_id}")
except Exception as auth_error:
    print(f"Authentication failed: {auth_error}")

# Path to file that will store the last mention ID
LAST_MENTION_FILE = 'last_mention_id.txt'

# Read the last mention ID from file, or use a default value
def get_last_mention_id():
    try:
        if os.path.exists(LAST_MENTION_FILE):
            with open(LAST_MENTION_FILE, 'r') as f:
                last_id = int(f.read().strip())
                print(f"Loaded last mention ID: {last_id}")
                return last_id
        else:
            print("No saved mention ID found, using default")
            return 1
    except Exception as e:
        print(f"Error reading last mention ID: {e}")
        return 1

# Save the last mention ID to file
def save_last_mention_id(mention_id):
    try:
        with open(LAST_MENTION_FILE, 'w') as f:
            f.write(str(mention_id))
            print(f"Saved last mention ID: {mention_id}")
    except Exception as e:
        print(f"Error saving last mention ID: {e}")

def respond_to_mentions():
    last_mention_id = get_last_mention_id()
    highest_id_seen = last_mention_id
    
    try:
        print(f"Fetching mentions since ID: {last_mention_id}")
        mentions = responder.get_users_mentions(
            id=bot_id,
            since_id=last_mention_id,
            user_auth=True
        )
        
        if mentions.data:
            print(f"Found {len(mentions.data)} new mentions")
            
            # Sort mentions by ID to process them in order
            sorted_mentions = sorted(mentions.data, key=lambda x: x.id)
            
            for mention in sorted_mentions:
                print(f"Processing mention ID: {mention.id}, Text: {mention.text}")
                
                # Update highest_id_seen immediately for each mention
                if mention.id > highest_id_seen:
                    highest_id_seen = mention.id
                    # Save the ID immediately after updating it
                    save_last_mention_id(highest_id_seen)
                
                is_reply = False
                if mention.referenced_tweets:
                    for ref in mention.referenced_tweets:
                        if ref.type == "replied_to":
                            is_reply = True
                
                if not is_reply and mention.author_id != bot_id:
                    try:
                        print("Attempting to reply...")
                        response = generate_response(mention.text)
                        print(f"Generated response: {response}")
                        
                        tweet = responder.create_tweet(
                            text=response,
                            in_reply_to_tweet_id=mention.id
                        )
                        print(f"Replied successfully with Tweet ID: {tweet.id}")
                    
                    except Exception as tweet_error:
                        print(f"Error while replying: {tweet_error}")
            
            print(f"Finished processing mentions. Last mention ID: {highest_id_seen}")
        else:
            print("No new mentions found.")
    
    except Exception as e:
        print(f"Error in main loop: {e}")