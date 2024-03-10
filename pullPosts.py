import praw

# Initialize PRAW with your credentials
reddit = praw.Reddit(client_id='MT3dJOzwjCZ9swH7_yaqtA',
                     client_secret='FjRI5qy8hhn8tQ8GB5D4kBDYohsY5w',
                     user_agent='grizzhacks by /u/Deadeye420')

# Specify the subreddit you want to pull posts from
subreddit = reddit.subreddit('news')

# Pull the top 1000 posts from the subreddit
top_posts = subreddit.top(limit=1)

allPost = []

# Iterate over the top posts and print their titles and scores
for post in top_posts:
    all = dict()
    title = post.title
    # Iterate over the comments of each post
    comments = []
    for comment in post.comments.list():
        try:
            comments.append(comment.body)
        except:
            continue
    all[title] = comments
    allPost.append(all)

print(all)
