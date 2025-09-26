from flask import Flask
app = Flask(__name__)

return '<p>Welcome!</p><p><a href="/about">About this app</a></p><p><a href="/contact">Contact</a></p>'
    return '<p>Hello, World, I am a Flask app!</p><p><a href="/about">About this app</a></p><p><a href="/contact">Contact</a></p>'

@app.route('/about')
def about():
    return '<p>This application is running on the Flask web framework.</p><p>Learn more about Flask at <a href="https://flask.palletsprojects.com/">https://flask.palletsprojects.com/</a></p><p><a href="/">Back to home</a></p>'

@app.route('/contact')
def contact():
    return '<p>Contact me at: your.email@example.com</p><p><a href="/">Back to home</a></p>' 