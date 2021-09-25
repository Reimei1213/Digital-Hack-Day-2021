from flask import Flask
app = Flask(__name__, static_folder=".", static_url_path="")

@app.route("/")
def index():
    return app.send_static_file("index.html")
    
@app.route("/hello")
def hello():
    return "Hello World from C9!"
    
app.run(host="0.0.0.0", port=8000, debug=True)