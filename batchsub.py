import praw
import os
from dotenv import load_dotenv
from prawcore.exceptions import ResponseException

def read_subreddits(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def bulk_subscribe(reddit, subreddits):
    try:
        # Test authentication
        reddit.user.me()
    except ResponseException as e:
        print(f"Authentication failed: {e}")
        print(f"Status code: {e.response.status_code}")
        print(f"Response body: {e.response.text}")
        return

    for subreddit in subreddits:
        try:
            reddit.subreddit(subreddit).subscribe()
            print(f"Subscribed to r/{subreddit}")
        except Exception as e:
            print(f"Failed to subscribe to r/{subreddit}: {str(e)}")

def main():
    load_dotenv()

    client_id = os.getenv('REDDIT_CLIENT_ID')
    client_secret = os.getenv('REDDIT_CLIENT_SECRET')
    username = os.getenv('REDDIT_USERNAME')
    password = os.getenv('REDDIT_PASSWORD')
    user_agent = os.getenv('REDDIT_USER_AGENT', "BulkSubscribeScript/1.0 by YourUsername")

    print(f"Client ID: {client_id[:5]}...") # Print first 5 chars for verification
    print(f"Client Secret: {client_secret[:5]}...") # Print first 5 chars for verification
    print(f"Username: {username}")
    print(f"Password: {'*' * len(password)}") # Don't print actual password
    print(f"User Agent: {user_agent}")

    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        username=username,
        password=password,
        user_agent=user_agent
    )

    try:
        print(f"Authenticated user: {reddit.user.me()}")
    except Exception as e:
        print(f"Authentication failed: {str(e)}")


    subreddits_file = "subreddits.txt"
    subreddits = read_subreddits(subreddits_file)

    bulk_subscribe(reddit, subreddits)

if __name__ == "__main__":
    main()