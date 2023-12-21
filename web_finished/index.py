from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from utils.convert_audio import convert
from utils.predict import predict

app = Flask(__name__)
CORS(app, origins="*")


@app.route("/")
def home():
    return render_template("react.html")


@app.route("/static/<path:path>")
def serve_static(path):
    return app.send_static_file(path)


@app.route("/api/prediction", methods=["POST", "OPTIONS"])
def submit_form():
    if "file" not in request.files:
        return {"prediction": "No file part"}

    file = request.files.get("file")
    temp_path = "audio.wav"
    file.save(temp_path)

    if file.filename == "":
        return {"prediction": "No selected file"}

    return jsonify({"prediction": predict(convert(temp_path))})
