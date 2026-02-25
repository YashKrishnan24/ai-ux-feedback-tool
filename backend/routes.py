from flask import Blueprint, jsonify, request
from backend.services.analyzer import (
    readability_score,
    cta_score,
    contrast_score,
    generate_suggestions
)

api = Blueprint("api", __name__)

@api.route("/analyze", methods=["POST"])
def analyze():
    data = request.json

    if not data:
        return jsonify({"error": "No input data provided"}), 400

    text = data.get("website_text")
    buttons = data.get("buttons")
    primary_color = data.get("primary_color")
    background_color = data.get("background_color")

    if not text or not buttons or not primary_color or not background_color:
        return jsonify({"error": "All fields are required"}), 400

    read = readability_score(text)
    cta = cta_score(buttons)
    contrast = contrast_score(primary_color, background_color)

    final_score = final_score = round((0.4 * read) + (0.3 * cta) + (0.3 * contrast), 2)

    suggestions = generate_suggestions(read, cta, contrast)

    return jsonify({
        "readability": read,
        "cta_score": cta,
        "contrast_score": contrast,
        "final_score": final_score,
        "suggestions": suggestions
    })