# discord needs
import discord
from discord.ext import commands
import LLMmodels
from handel_regulations import history_game_regulations
# from handel_regulations import all_string_game_regulations
import json
import random

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

with open('setting.json', 'r', encoding='utf8') as jfile:
    DC_BOT_TOKEN = json.load(jfile)['TOKEN']


@bot.event
# when bot is online
async def on_ready():
    print(f"Ready bot --> {bot.user}")

'''
# 串接local gpt4all api
@bot.command()
async def Q(ctx, *, arg):
    if ctx.channel.id == 1210695777169711187:
        order_number = str(random.uniform(0,1))[2:7]
        await ctx.send(f'已接收到您的問題,我正在思考答案,您的問題編號是{order_number},請稍後！') 
        
        regulation = f"你現在是一個遊戲名叫天空之城的遊戲嚮導,你必須根據以下的知識回答接下來的問題,{all_string_game_regulations()},現在請你回答以下的問題。"
        ans = LLMmodels.mistral_completion(regulation + arg)

        await ctx.send(f'問題編號{order_number}:\n {ans}') 
'''


@bot.command()
async def Q(ctx, *, arg):
    if ctx.channel.id in [1210695777169711187, 714725643765415958]:
        order_number = str(random.uniform(0, 1))[2:7]
        username = ctx.author.nick
        await ctx.send(f'已接收到 ***{str(username)}***  的問題,我正在思考答案,您的問題編號是{order_number},請稍後！')

        history = history = [
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
        ans = LLMmodels.gemini_chat(history, prompt=arg)

        await ctx.send(f'問題編號{order_number}的回答:\n{ans}')


bot.run(DC_BOT_TOKEN)
