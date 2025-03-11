
import requests
import json
"""
URL: 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
Headers: {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
Input json: { "raw_document": { "text": text_to_analyse } }
"""
def emotion_detector(text: str):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    params =   { "raw_document": { "text": text} }
    response = requests.post(url, headers=headers, json=params)
    response_vals = json.loads(response.text)
    emotions = {}
    emotions = response_vals["emotionPredictions"][0]["emotion"]
    max_val = 0
    d_em = ""
    for key in emotions.keys():
        if emotions[key] > max_val:
            max_val = emotions[key]
            d_em = key
    emotions["dominant_emotion"] = d_em
    return emotions