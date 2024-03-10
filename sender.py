import requests
def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandbox5497b5a60014448990a9ab8a8908fde1.mailgun.org/messages",
        auth=("api", "692534629a3ec511f028ba6b3614f500-2c441066-9ff376b2"),
        data={"from": "RedditSummarizer <postmaster@sandbox5497b5a60014448990a9ab8a8908fde1.mailgun.org>",
            "to": "David Cirenese <davidcirenese@yahoo.com>",
            "subject": "Hello David Cirenese",
            "text": "Congratulations David Cirenese, you just sent an email with Mailgun! You are truly awesome!"})
send_simple_message()