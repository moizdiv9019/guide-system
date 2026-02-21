import google.generativeai as genai
import json

def Ai_Model(prompt, user_data,api,modell):

    try:
        client = genai.Client(api_key=api)

        json_userdata = json.dumps(user_data)

        response = client.models.generate_content(
             model=modell,
             #ai models used  
             #gemini-2.5-flash-lite
             #gemini-3-flash-preview
            contents=[prompt, json_userdata],
            config={'response_mime_type': 'application/json'}
        )

        data = json.loads(response.text)

        return {
            "status": "success",
            "data": data
        }

    except Exception as e:

        error_msg = str(e).lower()

        if "400" in error_msg:
            msg = "API key error try again after same time "
        elif "401" in error_msg or "403" in error_msg:
            msg = "API key error try again after same time"
        elif "429" in error_msg:
            msg = "Rate limit reached try again after same time"
        elif "500" in error_msg:
            msg = "Server error try again after same time"
        elif "503" in error_msg:
            msg = "Service unavailable try again after same time"
        elif "504" in error_msg:
            msg = "Timeout error try again after same time"
        else:
            msg = e

        return {
            "status": "error",
            "message": msg
        }






