from flask import Flask, render_template, request
import pickle
from pathlib import Path

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "spam_model.pkl"
VECTORIZER_PATH = BASE_DIR / "vectorizer.pkl"

# Load model & vectorizer once
with open(MODEL_PATH, "rb") as model_file:
    model = pickle.load(model_file)

with open(VECTORIZER_PATH, "rb") as vectorizer_file:
    cv = pickle.load(vectorizer_file)


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    user_input = request.form.get("message", "")

    data = cv.transform([user_input])
    result = model.predict(data)[0]

    output = "Spam ❌" if result == 1 else "Not Spam ✅"

    return render_template("index.html", prediction=output)


if __name__ == "__main__":
    print("🚀 Flask server starting...")
    app.run(debug=True, port=5001)