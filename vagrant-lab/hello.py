from flask import Flask
app = Flask(__name__)

@app.route('/')
def say_hello():
    return '<p>Hello, World, I am a Flask app!</p><p><a href="/about">About this app</a></p><p><a href="/contact">Contact</a></p>'

@app.route('/about')
def about():
    return '<p>This application is running on <a href="https://www.python.ord">Python<a> and the Flask web framework.</p><p>Learn more about Flask at <a href="https://flask.palletsprojects.com/">https://flask.palletsprojects.com/</a></p><p><a href="/">Back to home</a></p>'

@app.route('/contact')
def contact():
    return '<p>Contact me at: your.email@example.com</p><p><a href="/">Back to home</a></p>'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)