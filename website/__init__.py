import os
from flask import Flask
from flask_socketio import SocketIO
import re


def create_app():
    application = Flask(__name__)
    socketio = SocketIO(application)

    # Read SECRET_KEY from environment for production safety; fall back to a dev key
    application.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'jjjjjjjj')

    from .views import views

    application.register_blueprint(views)

    @socketio.on('textarea_update')
    def handle_textarea_update(data):
        text = data["text"]
        matches = re.findall(r'\[(.*?)\]', text)
        socketio.emit('render_matches', {'matches': matches})

    return application, socketio