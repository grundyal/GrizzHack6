from flask import Flask, render_template, request, redirect, url_for
import mariadb

app = Flask(__name__)
app.config["DEBUG"] = True

# configuration used to connect to MariaDB
config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'password',
    'database': 'grizzhack'
}


test =[
    {
        "eventSummary": "A user shares their progress pictures after 6 months of using minoxidil and finasteride",
        "redditReaction": "The Reddit community praises the user for their progress and shares encouraging comments. Many users express their happiness for the OP and some share their own success stories with minoxidil and finasteride."
    },
    {
        "eventSummary": "A user asks for advice on dealing with shedding caused by minoxidil",
        "redditReaction": "Reddit users provide supportive advice and suggestions to help the user cope with shedding. Some users recommend sticking with the treatment despite shedding, while others suggest incorporating dermarolling into the routine."
    },
    {
        "eventSummary": "A user shares their experience of severe scalp irritation from a new shampoo",
        "redditReaction": "The Reddit community sympathizes with the user and offers various solutions to alleviate the scalp irritation. Suggestions include switching to a different shampoo, using conditioner, or seeking advice from a dermatologist for specific treatments."
    }
]


@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/submit', methods=['POST'])
def submit():

    email = request.form.get('email')
    subreddit = request.form.get('subreddit')
    firstname = request.form.get('fname')
    lastname = request.form.get('lname')

    # Process the email and subreddit values as needed
    # For example, you can send an email, store in a database, etc.

    # Call the Python function to handle the data
    process_data(email, subreddit, firstname, lastname)

    return redirect(url_for('results', subreddit=subreddit))

def process_data(email, subreddit, firstname, lastname):
    conn = mariadb.connect(**config)
    # create a connection cursor
    cur = conn.cursor()
    query = f"INSERT INTO info (email, subreddit, fname, lname) VALUES ('{email}', '{subreddit}', '{firstname}', '{lastname}')"
    cur.execute(query)

    # Add your processing logic here
    # For instance, you can send an email, save to a database, etc.

    conn.commit() 
    conn.close() 

@app.route('/results')
def results():
    subreddit_param = request.args.get('subreddit')
    return render_template('results.html', test=test, subreddit=subreddit_param)

if __name__ == '__main__':
    app.run(debug=True)