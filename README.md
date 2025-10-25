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

## Deploy to Elastic Beanstalk

1. Ensure `requirements.txt`, `Procfile`, and `.ebextensions/python.config` are present at the project root.
2. Install EB CLI and initialize:

```powershell
pip install awsebcli
eb init -p python-3.11 my-template-editor --region us-east-1
```

3. Create environment and deploy:

```powershell
eb create my-template-editor-env --single --instance_type t2.micro
eb deploy
eb open
```

## GitHub

1. Add files and commit:

```powershell
git init
git add .
git commit -m "Initial commit: Template Editor"
```

2. Push to GitHub (create repo first on GitHub):

```powershell
git remote add origin https://github.com/<your-user>/<repo-name>.git
git branch -M main
git push -u origin main
```

## Notes

- SECRET_KEY is read from the `SECRET_KEY` environment variable when available.
- The app uses Gunicorn + Eventlet for websocket support in production. Do not leave debug enabled on EB.
- If you scale to multiple instances, configure a message queue (Redis) for Socket.IO message passing or enable sticky sessions.
