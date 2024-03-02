from handel_regulations import history_game_regulations

def chat_history():
    history = [
            {
                "role": "user",
                "parts": ['你現在是一個遊戲名叫天空之城的遊戲嚮導,你必須記住我告訴你的所有知識並根據以下我告訴你的知識回答接下來的問題。']
            },
            {
                "role": "model",
                "parts": ['好的,我會開始記住接下來你說的內容。']
            },
            *history_game_regulations(),
            {
                "role": "user",
                "parts": ['現在請你回答以下的問題,開頭的回答請用"根據我所知道的知識",而不知道的問題請回答"我不知道"。']
            },
            {
                "role": "model",
                "parts": ['好的,請問問題是什麼?']
            },
        ]
    
    return history
