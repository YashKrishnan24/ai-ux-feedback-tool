import textstat

def readability_score(text):
    score = textstat.flesch_reading_ease(text)
    return round(max(0, min(score, 100)), 2)


def cta_score(buttons):
    strong_words = ["buy", "start", "join", "try", "download", "explore", "get"]
    score = 0

    for word in buttons.lower().split(","):
        for strong in strong_words:
            if strong in word.strip():
                score += 20

    return min(score, 100)


def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def contrast_score(color1, color2):
    r1, g1, b1 = hex_to_rgb(color1)
    r2, g2, b2 = hex_to_rgb(color2)

    brightness1 = (299*r1 + 587*g1 + 114*b1) / 1000
    brightness2 = (299*r2 + 587*g2 + 114*b2) / 1000

    diff = abs(brightness1 - brightness2)
    return min(int(diff), 100)


def generate_suggestions(read, cta, contrast):
    suggestions = []

    if read < 50:
        suggestions.append("Improve readability by shortening sentences.")

    if cta < 40:
        suggestions.append("Use stronger action verbs in CTA buttons.")

    if contrast < 50:
        suggestions.append("Increase color contrast for accessibility.")

    return suggestions