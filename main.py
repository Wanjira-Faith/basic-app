from flask import Flask

# Create Flask application instance
app = Flask(__name__)

# Define a route for the root URL '/'
@app.route('/')
def index():
    return '<h2>This is the homepage</h2>'

# Define a route for '/tuna'
@app.route('/tuna')
def tuna():
    return '<h2>Tuna is good </h2>'

# Define a dynamic route with a placeholder variable 'username'
@app.route('/profile/<username>')
def profile(username):
    # Extract the 'username' varibale from the URL and include it in the HTML response
    return '<h2>Hey there %s </h2>' %username

# Check if the script is being run as the main program
if __name__ == '__main__':
    # Start flask application in debug mode
    app.run(debug=True)