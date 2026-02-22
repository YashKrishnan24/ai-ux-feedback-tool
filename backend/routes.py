from flask import Blueprint, jsonify, request
from backend.services.analyzer import readability_score

api = Blueprint("api", __name__)

@api.route("/")
def home():
    return jsonify({"message": "Backend working properly!"})

@api.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    text = data.get("website_text")

    if not text:
        return jsonify({"error": "Text is required"}), 400

    score = readability_score(text)

    return jsonify({
        "readability_score": score
    })