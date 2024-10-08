# Reddit Bulk Subreddit Subscriber

This Python script allows you to bulk subscribe to a list of subreddits using the Reddit API.

## Prerequisites

- Python 3.6 or higher
- A Reddit account
- A Reddit API application (script type)

## Setup

1. Clone this repository or download the source code.

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Create a Reddit API application:
    - Go to https://www.reddit.com/prefs/apps
    - Click on "Create App" or "Create Another App" at the bottom of the page
    - Fill in the following details:
        - Name: Choose a name for your script (e.g., "BulkSubscribeScript")
        - App type: Select "Script"
        - Description: Optional, but you can briefly describe what your script does
        - About URL: This is optional for script-type apps, you can leave it blank
        - Redirect URI: Enter `http://localhost:8080`
          (Note: This won't be used by the script, but Reddit requires a value)
    - Click "Create app"

4. After creating the app, note down the following:
    - Client ID: The string under the app name
    - Client Secret: Click "edit" and you'll see the secret

5. Rename the `.env.sample` file to `.env` and fill in your details:
   ```
   REDDIT_CLIENT_ID=your_client_id_here
   REDDIT_CLIENT_SECRET=your_client_secret_here
   REDDIT_USERNAME=your_reddit_username
   REDDIT_PASSWORD=your_reddit_password
   REDDIT_USER_AGENT=BulkSubscribeScript/1.0 by YourUsername
   ```
   Replace `YourUsername` in the user agent with your actual Reddit username.

6. Create a file named `subreddits.txt` in the same directory as the script. Add each subreddit you want to subscribe to on a new line, without the "r/" prefix. For example:
   ```
   AskReddit
   funny
   aww
   ```

## Usage

Run the script using Python:

```
python batchsub.py
```

The script will attempt to subscribe to each subreddit listed in `subreddits.txt` and print the results.

## Troubleshooting

If you encounter any issues:

1. Ensure your Reddit account credentials are correct and the account is not locked or requiring additional verification.
2. Verify that the Client ID and Client Secret are correct and belong to a script-type app.
3. Make sure your Reddit account has two-factor authentication (2FA) disabled.
4. Check if your Reddit account has been suspended or if there are any restrictions on it.
5. Ensure your system's time is correctly synchronized.

If problems persist, try creating a new Reddit API application or create an issue here on Github.

## Security Note

Keep your `.env` file secure and never share it publicly, as it contains sensitive information.

## Disclaimer

This script is for educational purposes only. Make sure to comply with Reddit's API terms of service and use the script responsibly.