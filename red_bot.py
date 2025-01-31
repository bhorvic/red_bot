import praw
from red_bot_config import username, password, client_id, client_secret

reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    username=username,
    password=password,
    user_agent='test_bot'
)

# Fetch top 5 posts from a subreddit
# subreddit = reddit.subreddit("learnpython")  # Change to any subreddit you want
# for post in subreddit.hot(limit=5):
#     print(f"Title: {post.title}, Upvotes: {post.score}, URL: {post.url}")

# Choose a subreddit (preferably a private or test subreddit)
# subreddit_name = "bhorvic"  # Change this to your test subreddit

# # Submit a text post
# submission = reddit.subreddit(subreddit_name).submit(
#     title="Test Post from PRAW",
#     selftext="This is a test post created using PRAW. 🚀"
# )

# print(f"Post created! URL: {submission.url}")

# post_id = "1i7d7s7"  # Replace with the actual post ID
# submission = reddit.submission(id=post_id)

# # Target username to reply to
# target_username = "sexyebola69"  # Replace with the actual username

# Loop through comments to find the specific user's comment
# for comment in submission.comments:
#     if comment.author and comment.author.name == target_username:
#         reply = comment.reply("Yeah, you and Claypoole really got after it that night. ;-)")
#         if reply:
#             print(f"Replied to {target_username}'s comment: {reply.id}")
#         else:
#             print(f"Failed to reply to {target_username}'s comment.")
#         break  # Stop after replying once
# Define target username
target_username = "bhorvic"  # Change this to the Reddit username

# Fetch user comments
user = reddit.redditor(target_username)

# Store unique post IDs
post_ids = set()

# Get the last 10 comments made by the user
for comment in user.comments.new(limit=10):
    post_ids.add(comment.submission.id)  # Extract post ID

# Print extracted post IDs
print("Posts the user commented on:")
for post_id in post_ids:
    print(f"https://www.reddit.com/comments/{post_id}")

# Loop through post IDs to reply to each post
for post_id in post_ids:
    submission = reddit.submission(id=post_id)
    for comment in submission.comments:
        if comment.author and comment.author.name == target_username:
            reply = comment.reply("haha! fart!")
            if reply:
                print(f"Replied to {target_username}'s comment: {reply.id}")
            else:
                print(f"Failed to reply to {target_username}'s comment.")
            break  # Stop after replying once