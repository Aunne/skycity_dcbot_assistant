import google.generativeai as genai
import json

with open('setting.json', 'r', encoding='utf8') as jfile:
    Gemini_API_KEY = json.load(jfile)['Gemini_API_KEY']


def gemini_chat(history, prompt):
    genai.configure(api_key=Gemini_API_KEY)

    # Set up the model
    generation_config = {
        "temperature": 0.9,
        "top_p": 0.4,
        "top_k": 10,
        "max_output_tokens": 2048,
    }

    safety_settings = {
        "block_unsafe_content": False,
        "enforce_content_policy": False,
        "filter_prohibited_content": False
    }

    model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                                  generation_config=generation_config)
    
    convo = model.start_chat(history=history)
    convo.send_message(prompt)

    if convo.last.text != "":
        return convo.last.text

    return "抱歉,我不明白你的意思。請重新表述你的問題。"
