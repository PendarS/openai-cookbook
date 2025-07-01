import os
from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'secret!')
socketio = SocketIO(app)

@app.route('/')
def index():
    """Serve the chat page."""
    return render_template('index.html')

@socketio.on('message')
def handle_message(msg):
    """Broadcast received messages to all clients."""
    send(msg, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
