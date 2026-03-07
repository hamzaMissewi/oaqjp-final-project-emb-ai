"""Server for Web Deployment"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector


app = Flask("Emotion Detector")


@app.route('/')
def render_homepage():
    """ Render homepage """
    return render_template("index.html")


@app.route('/emotionDetector', methods=["GET"])
def emotion_analysis() -> str:
    """ Analyze text and return emotion detection (analysis result) """
    text_to_analyze = request.args["textToAnalyze"]
    analysis_result = emotion_detector(text_to_analyze)

    # Required output format:
    # For the given statement, the system response is '<emotion1>': <score1>,
    # '<emotion2>': <score2>, '<emotionN>': <scoreN>. The dominant emotion is <emotion>.
    #
    # Required output format when dominant_emotion == None:
    # Invalid text! Please try again.
    if analysis_result["dominant_emotion"] is None:
        response = "Invalid text! Please try again!"
    else:
        response = "For the given statement, the system response is"

        for key, value in analysis_result.items():
            # dominant emotion is mentioned separately as its own sentence.
            if key != "dominant_emotion":
                response += f" '{key}': {value},"

        # Replace last comma with point. If index is -1, no commas found.
        last_comma_index = response.rfind(",")
        if last_comma_index != -1:
            response = response[:last_comma_index] + '.' + response[last_comma_index + 1:]

        response += f" The dominant emotion is {analysis_result['dominant_emotion']}."

    return response


@app.route("/emotionDetector2")
def emotion_analyzer():
    '''Retrieve the provided text string from the user, then pass the text
    to be analyzed by the emotion detector. Finally, return a response displaying
    the confidence scores across all emotions and the dominant emotion.
    '''
    text_to_analyse = request.args.get('textToAnalyze')
    emotion_result = emotion_detector(text_to_analyse)
    anger = emotion_result['anger']
    disgust = emotion_result['disgust']
    fear = emotion_result['fear']
    joy = emotion_result['joy']
    sadness = emotion_result['sadness']
    dominant_emotion = emotion_result['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again"

    response_str = f"""For the given statement, the system response is
    'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}, 'sadness': {sadness}.
    The dominant emotion is <strong>{dominant_emotion}</strong>."""
    return response_str

@app.route("/")
def render_index_page():
    '''Render the index page to the user, this is where the text string to be
    analyzed is provided and a response is displayed back to the user.
    '''
    return render_template('index.html')

# To make sure that the server only runs when the script is executed
# directly (not imported as a module)
if __name__ == "__main__":
    app.run(debug = True)
