from flask import Flask, request
import json
import pandas as pd
import urllib
import xml.etree.ElementTree as ET

app = Flask(__name__, static_folder=".", static_url_path="")
main_df = pd.read_csv("./data/data_v2.csv")
label_df = pd.read_csv("./data/label_v2.csv")

# @app.route("/")
# def index():
#     return app.send_static_file("index.html")
    
@app.route("/hello")
def hello():
    return "Hello World from C9!"
    
@app.route("/json")
def res_json():
    with open("./style.json") as f:
        json_body = json.loads(f.read())
        return json_body
    
@app.route("/crimeinfo/<tag>")
def crimeinfo(tag):
    red, yello, blue = [], [], []
    for i, row in main_df.iterrows():
        counter = int(row[tag])
        pref_id = int(row["id"])
        if counter >= 500:
            red.append(pref_id)
        elif counter >= 100:
            yello.append(pref_id)
        else:
            blue.append(pref_id)
            
    fill_colors = ["match", ["id"]]
    if len(red) > 0:
        fill_colors.append(red)
        fill_colors.append("hsl(0, 83%, 55%)")
    if len(yello) > 0:
        fill_colors.append(yello)
        fill_colors.append("hsl(64, 83%, 55%)")
    if len(blue) > 0:
        fill_colors.append(blue)
        fill_colors.append("hsl(232, 83%, 55%)")
    fill_colors.append("hsl(87, 83%, 55%)")
            
    
    layer_source = {
        "id": "boundaries-admin-3 (1)",
        "type": "fill",
        "source": "composite",
        "source-layer": "boundaries_admin_3",
        "layout": {},
        "paint": {
            "fill-color": fill_colors,
            "fill-opacity": ["case", ["==", ["id"], 0], 1, 1]
        }
    }

    layer_source2 = {
        "id": "boundaries-admin-3-line",
        "type": "line",
        "source": "composite",
        "source-layer": "boundaries_admin_3",
        "layout": {},
        "paint": {}
    }
        
    with open("./style_tepl.json") as f:
        json_body = json.loads(f.read())
        json_body["layers"].append(layer_source)
        json_body["layers"].append(layer_source2)
        return json_body
    
@app.route("/yahoo/<lat>/<lon>")
def yahooApi(lat, lon):
    url = "https://map.yahooapis.jp/geocode/V1/geoCoder?appid=dj00aiZpPWE5ZldCOTlTbmZMcCZzPWNvbnN1bWVyc2VjcmV0Jng9YWM-&al=2&ar=eq&lat=" + lat + "&lon=" + lon
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        xmlData = response.read()
        root = ET.fromstring(xmlData)
        text = ""
        if int(root[0][1].text) > 0:
            text = root[1][2].text
        print(text)
    return text


@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response
    

app.run(host="0.0.0.0", port=8000, debug=True)