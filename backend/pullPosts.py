import praw
import json  
from openai import OpenAI
import time

client = OpenAI(api_key = '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')

query = """
    For each event in you dataset, provide add to the list in the following format including an event summary and reddit reaction. Do this for at least three events.
    Do not include any explanations, only provide a RFC8259 compliant JSON response  following this format without deviation.
    [{
    "eventSummary": "summary of the event",
    "redditReaction": "in-depth description of reddit's reaction to the event"
    }]
"""

def returnPrompt(title):
    return 'How is Reddit responding to the recent news that {}?'.format(title)

def pullRedditsPostAndAiResponse(subredditName = 'news'):
    # Initialize PRAW with your credentials
    reddit = praw.Reddit(client_id='MT3dJOzwjCZ9swH7_yaqtA',
                        client_secret='FjRI5qy8hhn8tQ8GB5D4kBDYohsY5w',
                        user_agent='grizzhacks by /u/Deadeye420')

    # Specify the subreddit you want to pull posts from
    subreddit = reddit.subreddit(subredditName)

    # Pull the top 1000 posts from the subreddit
    top_posts = subreddit.hot(limit=10)

    dataWrapper = {}
    data = []

    count = 0
    for post in top_posts:
        for comment in post.comments.list():
            try:
                datum = {}
                datum['id'] = count
                datum['question'] = returnPrompt(post.title)
                datum['answer'] = comment.body
                data.append(datum)
                count += 1
            except:
                continue

    with open('data.json', 'w') as f:
        dataWrapper["data"] = data
        json.dump(dataWrapper, f)

    file = client.files.create(
        file=open("data.json", "rb"),
        purpose='assistants'
    )

    assistant = client.beta.assistants.create(
        name="Event Analysis Assistant 4",
        instructions="you are an assistant that is going to interpret reddits replies to certain events being posted in the subreddit {}. First, for each important event, give a summary of the event and then another separate in depth summary of reddit's reaction.".format(subredditName),
        model="gpt-3.5-turbo",
        tools=[{"type": "retrieval"}],
        file_ids=[file.id]
    )   

    attemptCount = 0
    while True:
        try:
            attemptCount += 1
            if attemptCount > 3:
                raise Exception("GPT-3.5 Turbo took too long to respond")

            thread = client.beta.threads.create(
            messages=[
                {
                "role": "user",
                "content": query,
                "file_ids": [file.id]
                }
            ]
            )

            run = client.beta.threads.runs.create(
                thread_id=thread.id,
                assistant_id=assistant.id
            )

            checkCount = 0
            while True:
                if checkCount > 3:
                    raise Exception("GPT-3.5 Turbo took too long to respond")
                run = client.beta.threads.runs.retrieve(
                    thread_id = thread.id,
                    run_id = run.id
                )
                time.sleep(5)
                checkCount += 1
                if run.status == "completed":
                    break

            messages = client.beta.threads.messages.list(
                thread_id = thread.id
            )

            response = messages.data[0].content[0].text.value
            # Check that gpt returned a valid response, else try again
            if response.count('eventSummary') < 2 or response.count('[') != 1 or response.count(']') != 1:
                continue

            start = response.find('[')
            end = response.find(']') + 1

            listString = response[start:end]
            list_of_dicts = json.loads(listString)
            return response
        except:
            
            continue