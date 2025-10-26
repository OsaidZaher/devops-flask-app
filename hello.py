from flask import Flask
import redis
import json
import time

app = Flask(__name__)

# Connect to Redis
r = redis.Redis(host='redis-server', port=6379, decode_responses=True)

@app.route('/')
def say_hello():
    data = r.get('home')
    if data is not None:
        data = json.loads(data)
        # 600 seconds == 10 minutes
        if time.time() - data['time'] <= 600:
            return data['html']
    
    # Original HTML content
    data = '<p>Hello, World, I am a Flask app!</p><p><a href="/about">About this app</a></p><p><a href="/contact">Contact</a></p>'
    
    r.set('home', json.dumps({
        'html': data,
        'time': time.time()
    }))
    
    return data

@app.route('/about')
def about():
    data = r.get('about')
    if data is not None:
        data = json.loads(data)
        # 600 seconds == 10 minutes
        if time.time() - data['time'] <= 600:
            return data['html']
    
    # Original HTML content
    data = '<p>This application is running on <a href="https://www.python.org">Python</a> and the Flask web framework.</p><p>Learn more about Flask at <a href="https://flask.palletsprojects.com/">https://flask.palletsprojects.com/</a></p><p><a href="/">Back to home</a></p>'
    
    r.set('about', json.dumps({
        'html': data,
        'time': time.time()
    }))
    
    return data

@app.route('/contact')
def contact():
    data = r.get('contact')
    if data is not None:
        data = json.loads(data)
        # 600 seconds == 10 minutes
        if time.time() - data['time'] <= 600:
            return data['html']
    
    # Original HTML content
    data = '<p>Contact me at: your.email@example.com</p><p><a href="/">Back to home</a></p>'
    
    r.set('contact', json.dumps({
        'html': data,
        'time': time.time()
    }))
    
    return data

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)