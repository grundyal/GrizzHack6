import requests
def send_simple_message(firstName, lastName, email, message, subreddit):
    htmlText = """<html><body><head>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                    }
                    h1 {
                        color: #333;
                        border-bottom: 1px solid #d0d0d0;
                    }
                    p {
                        text-align: justify;
                        line-height: 1.6;
                    }
                </style>
            </head>"""
    htmlText += '<h1>Reddit Summarizer for r/{}</h1>'.format(subreddit)
    for i in range(0, len(message)):
        header = '<h2>Event {}: {}</h1>'.format(i+1, message[i].get("eventSummary"))
        body = '<p>Reddit\'s reaction: {}</p><br></br>'.format(message[i].get("redditReaction"))
        htmlText += header + body
    print(htmlText)
    return requests.post(
        "https://api.mailgun.net/v3/sandbox5497b5a60014448990a9ab8a8908fde1.mailgun.org/messages",
        auth=("api", "692534629a3ec511f028ba6b3614f500-2c441066-9ff376b2"),
        data={"from": "RedditSummarizer <postmaster@sandbox5497b5a60014448990a9ab8a8908fde1.mailgun.org>",
            "to": "{} {} <{}>".format(firstName, lastName, email),
            "subject": "Hello {}, {}".format(firstName, lastName),
            "html": """{}</body></html>""".format(htmlText)
            })