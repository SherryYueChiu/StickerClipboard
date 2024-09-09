import requests
import os

startId=124819206
endId=124819229
folderName='ㄇㄚˊ幾兔-賣萌大作戰'

os.makedirs('./allSticker/'+folderName+'/',exist_ok=True)

for stickerId in range(startId,endId):
    stickerId=str(stickerId)
    # low resolution
    # url='https://stickershop.line-scdn.net/stickershop/v1/sticker/'+stickerId+'/android/sticker.png'
    # high resolution
    url='https://stickershop.line-scdn.net/stickershop/v1/sticker/'+stickerId+'/iPhone/sticker@2x.png'
    r=requests.get(url)
    with open('./allSticker/'+folderName+'/'+stickerId+'.png','wb') as f:
        f.write(r.content)