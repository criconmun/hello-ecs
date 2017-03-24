from flask import Flask, render_template
import os, requests

app = Flask(__name__)

@app.route("/")
def hello():
    try:
        r = requests.get(os.environ.get('BACKEND_URL')).text
    except:
        r = 'Something went pear shaped!'
    return render_template('index.html', motd=r)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
