import requests
import json
import subprocess
from pyrogram import filters

#i think no need this line's 
#@Client.on_message(filters.edited)
#def on_edited(client, message):
    
from pyrogram import Client, filters
from pyrogram.types import Message    
#chages
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait
from pyromod import listen
from pyrogram.types import Message
import pyrogram
from pyrogram import Client, filters
import tgcrypto
from p_bar import progress_bar
# from details import api_id, #api_hash, bot_token
from subprocess import getstatusoutput
import helper
import logging
import time
import aiohttp
import asyncio
import aiofiles
from pyrogram.types import User, Message
# import progressor 
# from progressor import progress_for_pyrogram
import sys
import re
import os
# import pycurl

bot = Client(
    "bot",
    bot_token=os.environ.get("BOT_TOKEN"),
    api_id=int(os.environ.get("API_ID")),
    api_hash=os.environ.get("API_HASH")
)
@bot.on_message(filters.command("start") & filters.private)
async def start_handler(client, message):
    await message.reply_text("Hᴇʟʟᴏ ɪᴍ ᴛxᴛ Fɪʟᴇ Dᴏᴡɴʟᴏᴀᴅᴇʀ\nPʀᴇss /pyro ᴛᴏ Dᴏᴡɴʟᴏᴀᴅ Lɪɴᴋs Lɪsᴛᴇᴅ Iɴ ᴀ ᴛxᴛ Fɪʟᴇ Iɴ Tʜᴇ Fᴏʀᴍᴀᴛ Nᴀᴍᴇ » Lɪɴᴋs\n\n[⚡️Pᴏᴡᴇʀᴇᴅ Bʏ Sʜɪᴠᴀ]")

#Mᴀᴅᴇ Bʏ Sʜɪᴠᴀ 

@bot.on_message(filters.command(["cancel"]))
async def cancel(_, message: Message):
    await message.reply_text("Cᴀɴᴄᴇʟɪɴɢ Aʟʟ Pʀᴏᴄᴇss Plᴢ Wᴀɪᴛ")
    global cancel
    cancel = True
    await message.edit("Cᴀɴᴄʟᴇᴅ")
    return

@bot.on_message(filters.command("restart"))
async def restart_handler(_, message: Message):
    await message.reply_text("Rᴇsᴛᴀʀᴛᴇᴅ!", True)
    os.execl(sys.executable, sys.executable, *sys.argv)
    
@bot.on_message(filters.command(["pyro"])& ~filters.private)
async def account_login(bot: Client, m: Message):
    await message.reply_text("Sᴇɴᴅ ᴛxᴛ Fɪʟᴇ")
    input: Message = await bot.listen(message.chat.id)
    x = await input.download()
    await input.delete(True)

    path = f"./downloads/{message.chat.id}"

    try:    
        with open(x, "r") as f:
            content = f.read()
        content = content.split("\n")
        links = []
        for i in content:
            links.append(i.split(":", 1))
        os.remove(x)
        # print(len(links))
    except:
        await message.reply_text("Iɴᴠᴀʟɪᴅ Fɪʟᴇ Iɴᴘᴜᴛ.")
        os.remove(x)
        return
       
    await message.reply_text(f"Tᴏᴛᴀʟ Lɪɴᴋs Fᴏᴜɴᴅ Aʀᴇ {len(links)}\n\nSᴇɴᴅ Fʀᴏᴍ Wʜᴇʀᴇ Yᴏᴜ Wᴀɴᴛ Tᴏ Dᴏᴡɴʟᴏᴀᴅ Iɴᴛɪᴛɪᴀʟ ɪs 0")
    input1: Message = await bot.listen(message.chat.id)
    raw_text = input1.text

    try:
        arg = int(raw_text)
    except:
        arg = 0
    
    await message.reply_text("Eɴᴛᴇʀ Bᴀᴛᴄʜ Nᴀᴍᴇ")
    input0: Message = await bot.listen(message.chat.id )
    raw_text0 = input0.text
    await message.reply_text("Eɴᴛᴇʀ Rᴇsᴏʟᴜᴛɪᴏɴ")
input2: Message = await bot.listen(message.chat.id)
raw_text2 = input2.text

await message.reply_text("Nᴏᴡ Sᴇɴᴅ Tʜᴇ Tʜᴜᴍʙ Uʀʟ\nEɢ » https://telegra.ph/file/d9e24878bd4aba05049a1.jpg\n\nOʀ Sᴇɴᴅ Nᴏ")
input6 = message = await bot.listen(message.chat.id)
raw_text6 = input6.text

thumb = input6.text
if thumb.startswith("http://") or thumb.startswith("https://"):
    getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
    thumb = "thumb.jpg"
else:
    thumb == "no"

if raw_text =='0':
    count =1
else:       
    count =int(raw_text)   
    try:
    for i in range(arg, len(links)):

        url = links[i][1]
        name1 = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@","").replace("*","").replace(".","").strip()

        
        if raw_text2 == "144":
            cmd = f'yt-dlp -F "{url}"'
            k = await helper.run(cmd)
            out = helper.vid_info(str(k))
            # print(out)
            if '256x144' in out:
                ytf = f"{out['256x144']}"
            elif '320x180' in out:
                ytf = out['320x180']    
            elif 'unknown' in out:
                ytf = out["unknown"]
                
    else:
        ytf = "no"

elif raw_text2 == "180":

    cmd = f'yt-dlp -F "{url}"'
    k = await helper.run(cmd)
    out = helper.vid_info(str(k))
    # print(out)              
    if '320x180' in out:
        ytf = out['320x180']
    elif '426x240' in out:
        ytf = out['426x240']
    elif 'unknown' in out:
        ytf = out["unknown"]
    else:
        ytf = "no"                        

elif raw_text2 == "240":

    cmd = f'yt-dlp -F "{url}"'
    k = await helper.run(cmd)
    out = helper.vid_info(str(k))
    # print(out)          
    if '426x240' in out:
        ytf = out['426x240']
    elif '426x234' in out:
        ytf = out['426x234']
    elif '480x270' in out:
        ytf = out['480x270']
    elif '480x272' in out:
        ytf = out['480x272']
    elif '640x360' in out:
        ytf = out['640x360']
    elif 'unknown' in out:
        ytf = out["unknown"]
    else:
        ytf = "no"

elif raw_text2 == "360":

    cmd = f'yt-dlp -F "{url}"'
    k = await helper.run(cmd)
    out = helper.vid_info(str(k))
    # print(out)             
    if '640x360' in out:
        ytf = out['640x360']
    elif '638x360' in out:
        ytf = out['638x360']
    elif '636x360' in out:
        ytf = out['636x360']
    elif '768x432' in out:
        ytf = out['768x432']
    elif '638x358' in out:
        ytf = out['638x358']
    elif '852x316' in out:
        ytf = out['852x316']
    elif '850x480' in out:
        ytf = out['850x480']
    elif '848x480' in out:
        ytf = out['848x480']
    elif '854x480' in out:
        ytf = out['854x480']
    elif '852x480' in out:
        ytf = out['852x480']
    elif '854x470' in out:
        ytf = out['852x470']  
    elif 'unknown' in out:
        ytf = out["unknown"]
    else:
        ytf = "no"

elif raw_text2 == "480":

if raw_text2 == "360":
    cmd = f'yt-dlp -F "{url}"'
    k = await helper.run(cmd)
    out = helper.vid_info(str(k))
    # print(out)
    if '854x480' in out:
        ytf = out['854x480']
    elif '852x480' in out:
        ytf = out['852x480']
    elif '854x470' in out:
        ytf = out['854x470']
    elif '768x432' in out:
        ytf = out['768x432']
    elif '848x480' in out:
        ytf = out['848x480']
    elif '850x480' in out:
        ytf = ['850x480']
    elif '960x540' in out:
        ytf = out['960x540']
    elif '640x360' in out:
        ytf = out['640x360']
    elif 'unknown' in out:
        ytf = out["unknown"]
    else:
        ytf = "no"
elif raw_text2 == "720":
    cmd = f'yt-dlp -F "{url}"'
    k = await helper.run(cmd)
    out = helper.vid_info(str(k))
    # print(out)
    if '1280x720' in out:
        ytf = out['1280x720']
    elif '1280x704' in out:
        ytf = out['1280x704']
    elif '1280x474' in out:
        ytf = out['1280x474']
    elif '1920x712' in out:
        ytf = out['1920x712']
    elif '1920x1056' in out:
        ytf = out['1920x1056']
    elif '854x480' in out:
        ytf = out['854x480']
    elif '640x360' in out:
        ytf = out['640x360']
    elif 'unknown' in out:
        ytf = out["unknown"]
    else:
        ytf = "no"
elif "player.vimeo" in url:
    if raw_text2 == '144':
        ytf= 'http-240p'
    elif raw_text2 == "240":
        ytf= 'http-240p'
    elif raw_text2 == '360':
        ytf= 'http-360p'
    elif raw_text2 == '480':
        ytf= 'http-540p'
    elif raw_text2 == '720':
        ytf= 'http-720p'
    else:
        ytf = 'http-360p'
else:
    ytf="no"

if ytf == "0":
    res = "0"
elif ytf == "no" or ytf == "mp4":
    res = "NA"
else:
    res = list(out.keys())[list(out.values()).index(ytf)]

name = f'{str(count).zfill(3)}) {name1} {res}'

if "youtu" in url:
    cmd = f'yt-dlp -o "{name}.%(ext)s" -f "bestvideo[height<={int(raw_text2)}]+bestaudio" --no-keep-video --remux-video mkv "{url}"'
elif "player.vimeo" in url:
    cmd = f'yt-dlp -f "{ytf}+bestaudio" --no-keep-video --remux-video mkv "{url}" -o "{name}.%(ext)s"'
elif "m3u8" or "livestream" in url:
    cmd = f'yt-dlp -f "{ytf}" --no-keep-video --remux-video mkv "{url}" -o "{name}.%(ext)s"'
elif ytf == "0" or "unknown" in out:
    cmd = f'yt-dlp -f "{ytf}" --no-keep-video --remux-video mkv "{url}" -o "{name}.%(ext)s"'
elif ".pdf" in url:
    cmd = "pdf"
elif "drive" in url:
    cmd = "pdf"
elif ytf == "no":
    cmd = f'yt-dlp -o "{name}.mp4" --no-keep-video --remux-video mkv "{url}"'
else:
    cmd = f'yt-dlp -f "{ytf}+bestaudio" --hls-prefer-ffmpeg --no-keep-video --remux-video mkv "{url}" -o "{name}.%(ext)s"'

try:
    Show = f"[⚡️Pᴏᴡᴇʀᴇᴅ Bʏ Sʜɪᴠᴀ]\n\nDᴏᴡɴʟᴏᴀᴅɪɴɢ » \n\nNᴀᴍᴇ » {name}_Shiva.mkv\n\nQᴜᴀʟɪᴛʏ » {raw_text2}\n\nUʀʟ » {url}"
    prog = await message.reply_text(Show)
    cc = f'{str(count).zfill(2)}.{name}({raw_text2})_Shiva.mkv\n\nBᴀᴛᴄʜ » {raw_text0}\n\nDᴏᴡɴʟᴏᴀᴅᴇᴅ Bʏ » Sʜɪᴠᴀ'
    cc1 =f'{str(count).zfill(2)}.{name1}({raw_text2})sʜɪᴠᴀ.mkv\n\nBᴀᴛᴄʜ » {raw_text0}\n\nDᴏᴡɴʟᴏᴀᴅᴇᴅ Bʏ » Sʜɪᴠᴀ'

    if cmd == "pdf" or "drive" in url:
        try:
            ka=await helper.download(url,name)
            await prog.delete (True)
            time.sleep(1)
            reply = await message.reply_text(f"Uᴘʟᴏᴀᴅɪɴɢ » {name}")
            time.sleep(1)
            start_time = time.time()
            await message.reply_document(ka,caption=cc1)
            count+=1
            await reply.delete (True)
            time.sleep(1)
            os.remove(ka)
            time.sleep(3)
        except FloodWait as e:
            await message.reply_text(str(e))
            time.sleep(e.x)
            continue

    elif cmd == "pdf" or ".pdf" in url:
        try:
            ka=await helper.aio(url,name)
            await prog.delete (True)
            time.sleep(1)
            reply = await message.reply_text(f"Uploading » {name}")
            time.sleep(1)
            start_time = time.time()
            await message.reply_document(ka, caption=f'{str(count).zfill(2)}{name1} {res}.pdf\nBᴀᴛᴄʜ » {raw_text0}')
            count+=1
            await reply.delete (True)
            time.sleep(1)
            os.remove(ka)
            time.sleep(3)
        except FloodWait as e:
            await message.reply_text(str(e))
            time.sleep(e.x)
            continue

    else:
        res_file = await helper.download_video(url,cmd, name)
        filename = res_file
        await helper.send_vid(bot, m,cc,filename,thumb,name,prog)
        count+=1
        time.sleep(1)

except Exception as e:
    await m.reply_text(f"Dᴏᴡɴʟᴏᴀᴅɪɴɢ Fᴀɪʟᴇᴅ ❌\n{str(e)}\nNᴀᴍᴇ » {name}\nLɪɴᴋ » {url}")
    continue
    except Exception as e:
    await message.reply_text(e)
await message.reply_text("Dᴏɴᴇ")    

    
@bot.on_message(filters.command(["jw"])& ~filters.private)
async def account_login(bot: Client, m: Message):
    await m.reply_text("Sᴇɴᴅ ᴛxᴛ Fɪʟᴇ")
    input: Message = await bot.listen(message.chat.id)
    x = await input.download()
    await input.delete(True)

    path = f"./downloads/{message.chat.id}"

    try:
        with open(x, "r") as f:
            content = f.read()
        content = content.split("\n")
        links = []
        for i in content:
            links.append(i.split(":", 1))
        os.remove(x)
        # print(len(links))
    except:
        await message.reply_text("Iɴᴠᴀʟɪᴅ Fɪʟᴇ Iɴᴘᴜᴛ.")
        os.remove(x)
        return

    await message.reply_text(f"Tᴏᴛᴀʟ Lɪɴᴋs Fᴏᴜɴᴅ Aʀᴇ {len(links)}\n\nSᴇɴᴅ Fʀᴏᴍ Wʜᴇʀᴇ Yᴏᴜ Wᴀɴᴛ Tᴏ Dᴏᴡɴʟᴏᴀᴅ Iɴᴛɪᴛɪᴀʟ ɪs 0")
    input1: Message = await bot.listen(message.chat.id)
    raw_text = input1.text

    try:
        arg = int(raw_text)
    except:
        arg = 0

    await m.reply_text("Eɴᴛᴇʀ Bᴀᴛᴄʜ Nᴀᴍᴇ")
    input0: Message = await bot.listen(message.chat.id)
    raw_text0 = input0.text
    
    await m.reply_text("Eɴᴛᴇʀ Rᴇsᴏʟᴜᴛɪᴏɴ")
    input2: Message = await bot.listen(message.chat.id)
    raw_text2 = input2.text

    await m.reply_text("Nᴏᴡ Sᴇɴᴅ Tʜᴇ Tʜᴜᴍʙ Uʀʟ\nEɢ » https://telegra.ph/file/d9e24878bd4aba05049a1.jpg\n\nOʀ Sᴇɴᴅ Nᴏ")
    input6 = message = await bot.listen(message.chat.id)
    raw_text6 = input6.text

    thumb = input6.text
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb == "no"

    if raw_text =='0':
        count =1
    else:
        count =int(raw_text)

    try:
        for i in range(arg, len(links)):
            url = links[i][1]
            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@","").replace("*","").replace(".","").strip()
            if "jwplayer" in url:
                headers = {
                    'Host': 'api.classplusapp.com',
                    'x-access-token': 'eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJpZCI6MzgzNjkyMTIsIm9yZ0lkIjoyNjA1LCJ0eXBlIjoxLCJtb2JpbGUiOiI5MTcwODI3NzQyODkiLCJuYW1lIjoiQWNlIiwiZW1haWwiOm51bGwsImlzRmlyc3RMb2dpbiI6dHJ1ZSwiZGVmYXVsdExhbmd1YWdlIjpudWxsLCJjb3VudHJ5Q29kZSI6IklOIiwiaXNJbnRlcm5hdGlvbmFsIjowLCJpYXQiOjE2NDMyODE4NzcsImV4cCI6MTY0Mzg4NjY3N30.hM33P2ai6ivdzxPPfm01LAd4JWv-vnrSxGXqvCirCSpUfhhofpeqyeHPxtstXwe0',
                    'user-agent': 'Mobile-Android',
                    'app-version': '1.4.37.1',
                    'api-version': '18',
                    'device-id': '5d0d17ac8b3c9f51',
                    'device-details': '2848b866799971ca_2848b8667a33216c_SDK-30',
                    'accept-encoding': 'gzip',
                }

                params = (
                    ('url', f'{url}'),
                )
                response1 = requests.get(f'{a}', headers=headers1)

url1 = ""
if "youtube" in url:
    if "list" in url:
        response = requests.get(url)
        soup = bs(response.text, "html.parser")

        head = response.headers
        headers1 = {"Range": "bytes=0-", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

        for i in soup.find_all("a"):
            if "download video" in str(i):
                a = i["href"]

        response1 = requests.get(f'{a}', headers=headers1)

        url1 = (response1.text).split("\n")[2]

#         url1 = b
    else:
        url1 = url

name = f'{str(count).zfill(3)}) {name1}'    
Show = f"Downloading:-\n\nName :- {name}\n\nUrl :- {url1}"
prog = await message.reply_text(Show)
cc = f'Title » {name1}.mkv\nCaption » {raw_text0}\nIndex » {str(count).zfill(3)}'

if "pdf" in url:
    cmd = f'yt-dlp -o "{name}.pdf" "{url1}"'
else:
    cmd = f'yt-dlp -o "{name}.mp4" --no-keep-video --remux-video mkv "{url1}"'

try:
    download_cmd = f"{cmd} -R 25 --fragment-retries 25 --external-downloader aria2c --downloader-args 'aria2c: -x 16 -j 32'"
    os.system(download_cmd)

    if os.path.isfile(f"{name}.mkv"):
        filename = f"{name}.mkv"
    elif os.path.isfile(f"{name}.mp4"):
        filename = f"{name}.mp4"
    elif os.path.isfile(f"{name}.pdf"):
    filename = f"{name}.pdf"  
#   filename = f"{name}.mkv"
    subprocess.run(f'ffmpeg -i "{filename}" -ss 00:01:00 -vframes 1 "{filename}.jpg"', shell=True)
    await prog.delete (True)
    reply = await message.reply_text(f"Uploading - {name}")
    try:
        if thumb == "no":
            thumbnail = f"{filename}.jpg"
        else:
            thumbnail = thumb
    except Exception as e:
        await message.reply_text(str(e))

    dur = int(helper.duration(filename))

    start_time = time.time()
    if "pdf" in url1:
        await message.reply_document(filename,caption=cc)
    else:
        await m.reply_video(filename,supports_streaming=True,height=720,width=1280,caption=cc,duration=dur,thumb=thumbnail, progress=progress_bar,progress_args=(reply,start_time) )
    count+=1
    os.remove(filename)

    os.remove(f"{filename}.jpg")
    await reply.delete (True)
    time.sleep(1)
except Exception as e:
    await m.reply_text(f"downloading failed ❌\n{str(e)}\nName - {name}\nLink - {url} & {url1}")
    continue 
except Exception as e:
    await message.reply_text(e)
await message.reply_text("Done")     
bot.run()
                
