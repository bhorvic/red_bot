# Reddit Bot using PRAW

## Overview
This project is a WIP Reddit bot built using the **PRAW** (Python Reddit API Wrapper) library. The bot can:
- Fetch recent posts from a subreddit
- Comment on specific posts or users
- Reply to comments based on keywords
- Extract post IDs for posts where a specific user has commented

## Features
- **Authenticate with Reddit API** using client credentials
- **Post a comment** on a specific Reddit post
- **Reply to a specific user** in a subreddit
- **Extract post IDs** where a user has commented
- **Store extracted data** into a CSV file for further analysis

## Requirements
Make sure you have these requirements satisfied:

- Python 3.7+
- `praw` library
- `pandas` (if using CSV export)

### Install Dependencies
```sh
pip install praw pandas
```

## Setup
### 1. Reddit API Credentials
To use the bot, you need to create a Reddit app:
1. Go to [Reddit Apps](https://www.reddit.com/prefs/apps)
2. Click **Create an App**
3. Choose "script" as the app type
4. Note down the **client ID**, **client secret**, and **user agent**

### 2. Configure Authentication
Modify the `praw` configuration in your script:
```python
import praw

reddit = praw.Reddit(
    client_id="your_client_id",
    client_secret="your_client_secret",
    username="your_reddit_username",
    password="your_reddit_password",
    user_agent="your_bot_name"
)
```

## Usage
### Fetch Posts and Comment
```python
subreddit = reddit.subreddit("test")
top_post = next(subreddit.hot(limit=1))
top_post.reply("This is a test comment from my bot!")
```

### Reply to a Specific User
```python
target_username = "specific_user"
for comment in top_post.comments:
    if comment.author and comment.author.name == target_username:
        comment.reply("Hey! This is a bot reply.")
        break
```

### Extract Post IDs Where a User Commented
```python
user = reddit.redditor("specific_user")
for comment in user.comments.new(limit=10):
    print(f"Post ID: {comment.submission.id}")
```

## Running the Script
To execute the bot, run:
```sh
red_bot.py
```

## Notes
- Test in **a private subreddit** before deploying publicly.
- Ensure compliance with **Reddit API rules** to avoid bans.
- Use **try-except** for error handling.

## Contributing
Feel free to open an issue or submit a pull request if you have improvements.

## License
This project is licensed under the MIT License.

