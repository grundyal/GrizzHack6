from flask import Flask, render_template, request, redirect, url_for, session
import mariadb
import requests

app = Flask(__name__)
app.config["DEBUG"] = True
app.secret_key = 'your_secret_key'  # Change this to a secure secret key

# Configuration used to connect to MariaDB
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

    # Store data in Flask session
    session['email'] = email
    session['subreddit'] = subreddit
    session['firstname'] = firstname
    session['lastname'] = lastname

    process_data(email, subreddit, firstname, lastname)

    # Redirect to the loading page
    return redirect(url_for('loading'))

def process_data(email, subreddit, firstname, lastname):
    conn = mariadb.connect(**config)
    cur = conn.cursor()
    query = f"INSERT INTO info (email, subreddit, fname, lname) VALUES ('{email}', '{subreddit}', '{firstname}', '{lastname}')"
    cur.execute(query)
    conn.commit()
    conn.close()

@app.route('/loading')
def loading():
    # Redirect to the results route with stored parameters
    return render_template('loading.html')
@app.route('/results')
def results():
    # Retrieve data from Flask session
    email = session.get('email')
    subreddit = session.get('subreddit')
    firstname = session.get('firstname')
    lastname = session.get('lastname')

    # Construct the API URL
    api_url = f"http://127.0.0.1:5000/api/data/{subreddit}/{email}/{firstname}/{lastname}"

    # Make the API request
    response = requests.get(api_url)

    # Render the results page
    return render_template('results.html', test=response.json(), subreddit=subreddit)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
