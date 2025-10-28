# Template Editor

A small Flask + Flask-SocketIO app for editing templates with bracketed placeholders.

## Demo
https://www.loom.com/share/94697c95b974486693c63790d3e2d6eb 
## Run locally

1. Create virtualenv and install:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. Run locally:

```powershell
python application.py
# or
# use gunicorn with eventlet
gunicorn -k eventlet -w 1 application:application
```

3. Open http://127.0.0.1:5001
- The app uses Gunicorn + Eventlet for websocket support in production. Do not leave debug enabled on EB.
- If you scale to multiple instances, configure a message queue (Redis) for Socket.IO message passing or enable sticky sessions.
