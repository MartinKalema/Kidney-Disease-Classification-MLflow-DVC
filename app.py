from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from kidneyDiseaseClassifier.utils.common import decodeImage
from kidneyDiseaseClassifier.pipeline.stage_05_prediction import PredictionPipeline

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self) -> None:
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)


@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route("/train", methods=["GET", "POST"])
@cross_origin()
def train():
    os.system("dvc repro")
    # os.system("python main.py")
    return "Training completed successfully."

@app.route("/predict", methods=["POST"])
@cross_origin()
def predict():
    image = request.json['image']
    decodeImage(image, clientApp.filename)
    result = clientApp.classifier.predict()
    return jsonify(result)



if __name__ == "__main__":
    clientApp = ClientApp()
    # app.run(host="0.0.0.0", port=80, debug=True) for Microsoft Azure
    app.run(host="0.0.0.0", port=8080, debug=True) # Amazon Web Services and localhost