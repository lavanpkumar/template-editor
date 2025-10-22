from website import create_app


application, socketio = create_app()

if __name__ == "__main__":
    try:
        # Run on port 5001 in case 5000 is in use
        socketio.run(application, port=5001, debug=True)
    except OSError as e:
        print(f"Could not start server. Port might be in use. Error: {e}")
        # Try alternate port
        print("Trying alternate port 5002...")
        socketio.run(application, port=5002, debug=True)