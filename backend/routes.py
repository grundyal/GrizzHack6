from flask import Flask, jsonify
from pullPosts import pullRedditsPostAndAiResponse
from sender import send_simple_message
import time
import atexit
from apscheduler.schedulers.background import BackgroundScheduler
import os
from pullAllCustomers import getAllCustomers


def manifest():
    getAllCustomers()

app = Flask(__name__)

@app.route('/api/data/<subreddit>/<email>/<firstName>/<lastName>', methods=['GET'])
def api_data(subreddit, email, firstName, lastName):
    aiResponse = pullRedditsPostAndAiResponse(subredditName = subreddit)
    print(aiResponse)
    send_simple_message(firstName, lastName, email, aiResponse, subreddit)
    return jsonify(aiResponse)

if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    if os.environ.get('WERKZEUG_RUN_MAIN') != 'true':
        scheduler.add_job(func=manifest, trigger="interval", seconds=10)
        scheduler.start()
    app.run(debug=True)