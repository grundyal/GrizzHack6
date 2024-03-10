from flask import Flask, jsonify
from pullPosts import pullRedditsPostAndAiResponse
from sender import send_simple_message
import time
import atexit
from apscheduler.schedulers.background import BackgroundScheduler
import os
from pullAllCustomers import getAllCustomers


def manifest():
    rows = getAllCustomers()
    for row in rows:
        aiResponse = pullRedditsPostAndAiResponse(subredditName = row[1])
        send_simple_message(row[2], row[3], row[0], aiResponse, row[1])

app = Flask(__name__)

@app.route('/api/data/<subreddit>/<email>/<firstName>/<lastName>', methods=['GET'])
def api_data(subreddit, email, firstName, lastName):
    aiResponse = pullRedditsPostAndAiResponse(subredditName = subreddit)
    send_simple_message(firstName, lastName, email, aiResponse, subreddit)
    return jsonify(aiResponse)

if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    if os.environ.get('WERKZEUG_RUN_MAIN') != 'true':
        scheduler.add_job(func=manifest, trigger="interval", seconds=100000)
        scheduler.start()
    app.run(debug=True)