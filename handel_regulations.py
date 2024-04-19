import os

dirPath = os.path.dirname(os.path.abspath(__file__))
regulation_list = os.listdir(dirPath+"/skycity_regulation")


def all_string_game_regulations():
    AllRegulations = ""

    for regulation_txt in regulation_list:
        with open(dirPath+"/skycity_regulation/"+regulation_txt) as f:
            lines = f.readlines()
            for line in lines:
                if line != "":
                    AllRegulations += line.replace("\n", "。")
        AllRegulations += "。"

    while "。。" in AllRegulations:
        AllRegulations = AllRegulations.replace("。。", "。")

    return AllRegulations


def history_game_regulations():
    AllRegulations = ""
    game_history = []

    for regulation_txt in regulation_list:
        with open(dirPath+"/skycity_regulation/"+regulation_txt) as f:
            lines = f.readlines()
            for line in lines:
                if line != "":
                    AllRegulations += line
        game_history.append(
            {
                "role": "user",
                "parts": [AllRegulations]
            }
        )
        game_history.append(
            {
                "role": "model",
                "parts": ['好的,記住了。']
            }
        )

    return game_history
