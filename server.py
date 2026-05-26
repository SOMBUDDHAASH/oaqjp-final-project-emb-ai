"""
Server module for the Emotion Detection application.
Provides a Flask web server with routes for analyzing text
and rendering the frontend interface.
"""
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector")
def get_emotion_detector():
    """
    Retrieves input text from web request arguments, executes emotion analysis
    via the EmotionDetection package, and returns a formatted string containing
    all parsed emotional scores or a dedicated error validation message.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    # Handle scenario where dominant_emotion evaluates to None (invalid text/blank)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again."

    # Return string response formatted precisely to the client's specifications
    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )


@app.route("/")
def render_index_page():
    """
    Renders the default root index HTML webpage template
    for the user application interface.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
