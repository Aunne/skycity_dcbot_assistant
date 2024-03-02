# discord needs
import os
import discord
from discord.ext import commands
import LLMmodels
from chat import chat_history
# from handel_regulations import all_string_game_regulations
import json

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

with open('setting.json', 'r', encoding='utf8') as jfile:
    DATA = json.load(jfile)
    DC_BOT_TOKEN = DATA['TOKEN']
    WHITE_CHANNELS = DATA['WHITE_CHANNELS']
    WHITE_MEMBER = DATA['WHITE_MEMBER']
    ENABLE_WHITE_CHANNELS = DATA['ENABLE_WHITE_CHANNELS']
    ENABLE_WHITE_MEMBERS = DATA['ENABLE_WHITE_MEMBERS']


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
    '''
    question to bot
    '''
    if  ENABLE_WHITE_CHANNELS and (ctx.channel.id not in WHITE_CHANNELS):
    # if user not in specified channel uses that command,then not to do command
        return
    await ctx.reply(f'已接收到您的問題,我正在思考答案,請稍後！')

    history = chat_history()
    ans = LLMmodels.gemini_chat(history, prompt=arg)

    await ctx.reply(ans)

@bot.command()
async def restart(ctx):
    '''
    restart bot
    '''
    if ENABLE_WHITE_MEMBERS and (ctx.author.id not in WHITE_MEMBER):
    # if user not in WHITE_MEMBER ,then not to do command
        return
    os.system('supervisorctl restart skycity_dc_assistant_bot')


bot.run(DC_BOT_TOKEN)
