# skycity_dcbot_assistant
download this project and use pyenv to get a venv
python version 3.11

# first,in venv cmd environment install those packge
pip install discord.py


**if you want to use local mistral model,then install this**
pip install openai

**if you want to use google Gemini online LLM,then install this**
pip install -q -U google-generativeai

# seconcd
creat a folder be named "skycity_regulation",in this,write txt set for bot reading

# third
creat a "setting.json"
content : 
{
    "TOKEN": "your_dc_bot_token",
    "Gemini_API_KEY": "your_Gemini_API_KEY"
}

# done 
start to run your bot
