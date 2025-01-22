from flask import Flask, request, render_template

app = Flask(__name__)

# Route for the home page
@app.route('/')
def hello():
    return render_template("login.html")

# User database for login
database = {'Swaroopa': 'swaroopa11'}

# Route for login
@app.route('/login', methods=['POST', 'GET'])
def login():
    name = request.form['username']
    pswd = request.form['password']
    if name not in database:
        return render_template("login.html", info='Invalid User Name')
    else:
        if database[name] != pswd:
            return render_template("login.html", info='Invalid Password')
        else:
            return render_template("home.html", name1=name)

# Route for the portfolio page
@app.route('/portfolio')
def portfolio():
    return render_template("index.html")

# Route for the contact page
@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/home')
def home():
    return render_template("home.html")

if __name__ == '__main__':
    app.run(debug=True)
