from flask import Flask
import subprocess

app = Flask(__name__)

@app.route("/")
def hello():
    hw = "Hello World!"
    return subprocess.run(["df", "-h"])

if __name__ == "__main__":
    app.run('0.0.0.0', 8000, debug=True)