from flask import Flask

app = Flask(__name__)

#route decorator -maps/route a url to the return value of the function
@app.route('/')
def index():
    return 'This is the homepage'

@app.route('/tuna')
def tuna():
    return '<h2>Tuna is good </h2>'

if __name__ == '__main__':
    app.run(debug=True)