from flask import Flask, send_from_directory
import scrapper_tv
app = Flask(__name__)

@app.route("/")
def hello():
    return "API programme TV Français"

@app.route("/api/<path:filename>")
def api(filename):
    return send_from_directory('web/api/programme_tv',
                               filename + '.json', as_attachment=False)

if __name__ == "__main__":
    scrapper_tv.main()
    app.run()
