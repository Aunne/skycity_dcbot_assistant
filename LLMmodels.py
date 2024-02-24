import google.generativeai as genai
import json


# if want to use local mistral LLM model,please remove those annotation
# import random
# import openai
# openai.api_base = "http://127.0.0.1:4891/v1"
# openai.api_key = "not needed for a local LLM"


with open('setting.json', 'r', encoding='utf8') as jfile:
    Gemini_API_KEY = json.load(jfile)['Gemini_API_KEY']


"""
def mistral_completion(prompt):
    # choose model
    model = "mistral-7b-openorca.q4_0"
# make amount of text
    text_amount = 1
# Make the API request
    response = openai.Completion.create(
        model=model,
        prompt=prompt,
        presence_penalty=1.7,
        frequency_penalty=1.4,
        max_tokens=200,
        temperature=0.2,
        top_p=0.6,
        n=text_amount,
        echo=True,
        stream=False
    ).choices[random.randrange(text_amount)].text.split("\n", 1)[1]

    return response
"""


def gemini_chat(history, prompt):
    genai.configure(api_key=Gemini_API_KEY)

    # Set up the model
    generation_config = {
        "temperature": 1,
        "top_p": 0.4,
        "top_k": 10,
        "max_output_tokens": 2048,
    }

    safety_settings = {
        "block_unsafe_content": False,
        "enforce_content_policy": False,
        "filter_prohibited_content": False
    }

    model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                  generation_config=generation_config)

    convo = model.start_chat(history=history)
    convo.send_message(prompt)

    if convo.last.text != "":
        return convo.last.text

    return "抱歉,我不明白你的意思。請重新表述你的問題。"
