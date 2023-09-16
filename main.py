from flask import Flask

app = Flask(__name__)

#route decorator -maps/route a url to the return value of the function
@app.route('/')
def index():
    return 'This is the homepage'

if __name__ == '__main__':
    app.run(debug=True)