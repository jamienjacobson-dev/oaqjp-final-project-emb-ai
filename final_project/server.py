from flask import Flask, render_template, request, make_response
from EmotionDetection import emotion_detector

app = Flask("EmotionDetectionApp",template_folder='../templates',static_folder="../static")

@app.route("/emotionDetector")
def get_emotions():
    text_to_analyze = request.args.get('textToAnalyze')
    emotions = emotion_detector(text_to_analyze)
    outString = "For the given statement, the system response is "
    outString += f"'anger': {emotions['anger']}, "
    outString += f"'disgust': {emotions['disgust']}, "
    outString += f"'fear': {emotions['fear']}, "
    outString += f"'joy': {emotions['joy']} and "
    outString += f"'sadness': {emotions['sadness']}. "
    outString += f"The dominent emotion is <b>{emotions['dominant_emotion']}<b>"
    return make_response(outString)

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)