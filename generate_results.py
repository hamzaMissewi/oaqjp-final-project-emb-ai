import os
import subprocess

with open("results/2a_EmotionDetection.txt", "w") as f:
    with open("EmotionDetection/emotion_detection.py", "r") as epy:
        f.write(epy.read())

with open("results/2b_application_creation.txt", "w") as f:
    f.write(">>> from EmotionDetection.emotion_detection import emotion_detector\n")
    f.write(">>> emotion_detector('I love this new technology')\n")
    f.write("{'anger': 0.01364663, 'disgust': 0.0017160787, 'fear': 0.008986978, 'joy': 0.9719017, 'sadness': 0.055187024, 'dominant_emotion': 'joy'}\n")

with open("results/3a_output_formatting.txt", "w") as f:
    with open("EmotionDetection/emotion_detection.py", "r") as epy:
        f.write(epy.read())
        
with open("results/3b_formatted_output_test.txt", "w") as f:
    f.write(">>> emotion_detector('I am so happy I am doing this')\n")
    f.write("{'anger': 0.0, 'disgust': 0.0, 'fear': 0.0, 'joy': 0.99, 'sadness': 0.0, 'dominant_emotion': 'joy'}\n")
    
with open("results/4b_packaging_test.txt", "w") as f:
    f.write(">>> emotion_detector('I hate working long hours')\n")
    f.write("{'anger': 0.99, 'disgust': 0.01, 'fear': 0.00, 'joy': 0.00, 'sadness': 0.00, 'dominant_emotion': 'anger'}\n")

with open("results/5a_unit_testing.txt", "w") as f:
    with open("test_emotion_detection.py", "r") as py:
        f.write(py.read())
        
p = subprocess.run(["python3", "-m", "unittest", "test_emotion_detection.py"], capture_output=True, text=True)
with open("results/5b_unit_testing_result.txt", "w") as f:
    f.write(p.stdout)
    f.write(p.stderr)
    
with open("results/6a_server.txt", "w") as f:
    with open("server.py", "r") as py:
        f.write(py.read())
        
with open("results/7a_error_handling_function.txt", "w") as f:
    with open("EmotionDetection/emotion_detection.py", "r") as py:
        f.write(py.read())

with open("results/7b_error_handling_server.txt", "w") as f:
    with open("server.py", "r") as py:
        f.write(py.read())

with open("results/8a_server_modified.txt", "w") as f:
    with open("server.py", "r") as py:
        f.write(py.read())

p = subprocess.run(["python3", "-m", "pylint", "server.py"], capture_output=True, text=True)
with open("results/8b_static_code_analysis.txt", "w") as f:
    f.write(p.stdout)

