from flask import Flask, render_template

# Create a Flask application
app = Flask(__name__)



# landing page and aurthintication 
@app.route('/aurth')
def aurthinticate():
    return render_template("aurth.html")


# ssh connnetion handling 
@app.route('/connect')
def connect():
    return 'for ssh connetion'


# log dashboard
@app.route('/dashboard')
def dashboard():
    # return 'dashboard'
    return render_template("index.html") 


# Run the Flask app if this script is the main program
if __name__ == '__main__':
    app.run()

