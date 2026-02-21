
# AI-Based Website UX Feedback Tool

An AI-assisted web application that evaluates the User Experience (UX) quality of beginner websites by analyzing readability, CTA effectiveness, and color contrast accessibility.

---

##  Project Overview

This tool allows users to input:

- Website main content text
- Button labels (Call-To-Action text)
- Primary color
- Background color

The system analyzes these inputs and generates:

-  Readability Score
-  CTA Effectiveness Score
-  Color Contrast Score
-  UX Improvement Suggestions
-  Overall UX Rating (0–100)

This project combines Web Development + Applied NLP + UX principles.

---

##  How It Works

### Readability Analysis
- Uses Flesch Reading Ease formula (via `textstat`)
- Checks sentence length and complexity
- Suggests improvements if text is too hard or too simple

###  CTA Effectiveness Analysis
- Detects action verbs (e.g., Buy, Start, Join, Download)
- Identifies weak or generic CTAs
- Scores based on action-oriented language strength

###  Color Contrast Analysis
- Converts HEX colors to RGB
- Calculates brightness difference
- Evaluates accessibility compliance
- Suggests improvements for better readability

###  Final UX Score
Weighted combination of:
- Readability
- CTA strength
- Color contrast

---

## Tech Stack

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Python
- Flask

### AI / NLP
- textstat
- Rule-based scoring logic
