""" Python Flask AI Application: Emotion Detctor App"""
from flask import Flask, render_template, request, make_response
from EmotionDetection import emotion_detector

app = Flask("EmotionDetectionApp",template_folder='../templates',static_folder="../static")

@app.route("/emotionDetector")
def get_emotions():
    """Return emotional analysis for a given string"""
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze:
        return " Invalid text! Please try again!."

    emotions = emotion_detector(text_to_analyze)
    out_string = "For the given statement, the system response is "
    out_string += f"'anger': {emotions['anger']}, "
    out_string += f"'disgust': {emotions['disgust']}, "
    out_string += f"'fear': {emotions['fear']}, "
    out_string += f"'joy': {emotions['joy']} and "
    out_string += f"'sadness': {emotions['sadness']}. "
    out_string += f"The dominent emotion is <b>{emotions['dominant_emotion']}<b>"
    return make_response(out_string)

@app.route("/")
def render_index_page():
    """Display home page"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
