
###################
####python 3.x#####
#discord.py==1.4.0#
###################

import discord
import requests

client = discord.Client()

@client.event
async def on_ready():
    print("봇이 성공적으로 실행되었습니다.")
    game = discord.Game('★~하는중에 표시될 네임 작성★')
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith('!실시간검색어') or message.content.startswith('!실검'):
        json = requests.get('https://www.naver.com/srchrank?frm=main').json()
        ranks = json.get("data")

        for r in ranks:
            rank = r.get("rank")
            keyword = r.get("keyword")
            await message.channel.send(str(rank) + ". " + str(keyword))
            if rank > 4:
                break


client.run('★TOKEN★')
