import praw
from llmGoogle import humoroize
from twitter import create_post
from logger import log_activity
import os
from dotenv import load_dotenv
from pathlib import Path
import json

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

username = os.environ.get("REDDIT_USERNAME")
password = os.environ.get("REDDIT_PASSWORD")
client_id = os.environ.get("REDDIT_CLIENT_ID")
client_secret = os.environ.get("REDDIT_CLIENT_SECRET")

reddit_instance  = praw.Reddit(
    client_id=client_id, 
    client_secret=client_secret,
    username=username, 
    password=password, 
    user_agent="A news feed Bot made by u/Theinit01"
)

subreddit = reddit_instance.subreddit("notthepyaaz")
top_posts = subreddit.rising(limit=10)

# Load posted post IDs from JSON file
json_file = 'posted_posts.json'
try:
    with open(json_file, 'r') as f:
        posted_posts = set(json.load(f))
except FileNotFoundError:
    posted_posts = set()


for post in top_posts:
    for post in top_posts:
        if not post.is_self:
            if post.id in posted_posts:
                continue
            
            try:
                url = post.url
                title = post.title
                funny_title = humoroize(title)
                tweet = funny_title + "\n\n" + url + "\n#Notthepyaaz #NothteOnion"
                create_post(tweet)
                #log_activity(f"Posted tweet with ID {post.id} - '{funny_title}'")
                posted_posts.add(post.id)
            except Exception as e:
                log_activity(f"Failed to post tweet with ID {post.id} - {e}")

# Save updated posted_posts set to JSON file
with open(json_file, 'w') as f:
    json.dump(list(posted_posts), f)

log_activity(f"Script executed. {len(posted_posts)} tweets were posted.")