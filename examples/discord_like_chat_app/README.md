# Discord-like Chat App Example

This example demonstrates how to create a very basic real-time chat web app using
[Flask](https://flask.palletsprojects.com/) and
[Flask-SocketIO](https://flask-socketio.readthedocs.io/). Messages are
broadcast to all connected users, giving an experience similar to a minimal
Discord channel.

## Setup

1. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Run the server:

   ```bash
   python app.py
   ```

3. Open your browser at `http://localhost:5000` and start chatting in multiple
   tabs or devices.

This example is intentionally simple, without authentication or multiple
channels, but it provides a foundation you can expand upon for more advanced
features.
