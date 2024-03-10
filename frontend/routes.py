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

    # Return a response, or redirect to another page if needed
    return "Data submitted successfully"

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
    return render_template('results.html')

if __name__ == '__main__':
    app.run(debug=True)