from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route("/")
def hello():
    return "API programme TV Français"

@app.route("/api/<path:filename>")
def api(filename):
    r = send_from_directory('web/api/programme_tv',
            filename + '.json', as_attachment=False)
    r.headers.add('Access-Control-Allow-Origin', '*')
    return r
