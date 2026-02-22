import textstat

def readability_score(text):
    score = textstat.flesch_reading_ease(text)
    return max(0, min(score, 100))