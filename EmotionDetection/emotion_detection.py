import requests
import json

def emotion_detector(text_to_analyze):
    """
    Sends a POST request to the Watson NLP Emotion Predict service,
    parses the response, extracts emotion scores, finds the dominant emotion,
    and returns a structured dictionary.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    response = requests.post(url, json=myobj, headers=headers)
    
    # Transform the raw text response into a Python dictionary
    formatted_response = json.loads(response.text)
    
    # Navigate the nested JSON structure to isolate the scores
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    
    # Compile the values back into a flat dictionary targeting our specific metrics
    emotion_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    
    # Calculate the dominant emotion by identifying the key with the maximum value
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    
    # Construct the final expected dictionary formatting output
    result = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
    
    return result