from flask import Flask, request, jsonify
import base64
import io
import wave
import numpy as np

app = Flask(__name__)

def calculate_pace(audio_file, user_response):
    """
    Calculate words per minute (WPM) based on the length of the audio and the number of words transcribed.
    """
    text = user_response
    word_count = len(text.split())
    
    # Assuming 1 minute for every 160 words transcribed
    with wave.open(audio_file, 'rb') as wf:
        duration_in_seconds = wf.getnframes() / wf.getframerate()
        duration_in_minutes = duration_in_seconds / 60
    
    # Calculate words per minute
    pace = word_count / duration_in_minutes
    return pace

def count_filler_words(audio_file, user_response):
    """
    Count the number of filler words like 'um', 'uh', 'like', etc., in the transcribed audio.
    """
    filler_words = ['um', 'uh', 'like', 'you know', 'so', 'actually']
    text = user_response
    
    filler_count = 0
    for word in filler_words:
        filler_count += text.split().count(word)
    
    return filler_count



def analyze_speech(audio_data, user_response):
    """
    Analyzes speech features such as pace, filler words, and more.
    audio_data: Base64 encoded audio string.
    Returns a dictionary with speech analysis results.
    """
    analysis = {}

    # Decode audio from base64
    audio_data = base64.b64decode(audio_data)  # Decode the base64 string into raw audio
    audio_bytes = io.BytesIO(audio_data)
    
    with wave.open(audio_bytes, 'rb') as wf:
        frames = wf.getnframes()
        audio_data = wf.readframes(frames)
        audio_data = np.frombuffer(audio_data, dtype=np.int16)
    
    # Extract speech features (e.g., words per minute)
    pace = calculate_pace(audio_bytes)
    filler_words_count = count_filler_words(audio_bytes)

    analysis['pace'] = pace
    analysis['filler_count'] = filler_words_count
    analysis['feedback'] = []

    if pace > 160:
        analysis['feedback'].append("You are speaking too fast. Try to slow down.")
    elif pace < 50:
        analysis['feedback'].append("You are speaking very slow. Try to talk faster.")

    if filler_words_count > 5:
        analysis['feedback'].append("Try to reduce filler words like 'um', 'uh', etc.")
    
    return analysis

@app.route('/analyze-speech', methods=['POST'])
def analyze_speech_route():
    data = request.get_json()
    audio_data = data.get('audio')

    if not audio_data:
        return jsonify({"error": "No audio data received"}), 400

    analysis = analyze_speech(audio_data)
    return jsonify(analysis)

if __name__ == "__main__":
    app.run(debug=True)
    