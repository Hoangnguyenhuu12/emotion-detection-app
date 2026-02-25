import requests
import json

def emotion_detector(text_to_analyze):
    # Task 7: Xử lý đầu vào rỗng
    if not text_to_analyze.strip():
        return {"anger": None, "disgust": None, "fear": None, "joy": None, "sadness": None, "dominant_emotion": None}

    url = 'URL_API_WATSON_CỦA_BẠN' # Thay bằng URL được cấp trong khóa học
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    
    response = requests.post(url, json=input_json, headers=headers)
    
    # Task 7: Xử lý lỗi 400
    if response.status_code == 400:
        return {"anger": None, "disgust": None, "fear": None, "joy": None, "sadness": None, "dominant_emotion": None}

    # Task 3: Format output
    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotions, key=emotions.get)
    emotions['dominant_emotion'] = dominant_emotion
    
    return emotions
