from flask import Flask, render_template, request, redirect, url_for
import mariadb
import requests

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
    process_data(email, subreddit, firstname, lastname)

    return redirect(url_for('results', subreddit=subreddit, email=email, firstname=firstname, lastname=lastname))

def process_data(email, subreddit, firstname, lastname):
    conn = mariadb.connect(**config)
    cur = conn.cursor()
    query = f"INSERT INTO info (email, subreddit, fname, lname) VALUES ('{email}', '{subreddit}', '{firstname}', '{lastname}')"
    cur.execute(query)
    conn.commit() 
    conn.close() 

@app.route('/results')
def results():
    subreddit_param = request.args.get('subreddit')
    email_param = request.args.get('email')
    firstname_param = request.args.get('firstname')
    lastname_param = request.args.get('lastname')
    api_url = "http://127.0.0.1:5000/api/data/{}/{}/{}/{}".format(subreddit_param,email_param,firstname_param,lastname_param)
    response = requests.get(api_url)
    return render_template('results.html', test=response.json(), subreddit=subreddit_param)

if __name__ == '__main__':
    app.run(debug=True, port = 5001)