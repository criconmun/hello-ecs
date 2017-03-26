from flask import Flask
import os

app = Flask(__name__)

@app.route("/backend")
def motd():
    return os.environ.get('MOTD', 'No message specified...')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
