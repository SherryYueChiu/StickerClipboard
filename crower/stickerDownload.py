import requests
import os

startId=780332969
endId=780333008
folderName='ㄇㄚˊ幾兔－奇形怪狀篇？！'

os.makedirs('./public/allSticker/'+folderName+'/',exist_ok=True)

for stickerId in range(startId,endId+1):
    stickerId=str(stickerId)
    # low resolution
    # url='https://stickershop.line-scdn.net/stickershop/v1/sticker/'+stickerId+'/android/sticker.png'
    # high resolution
    url='https://stickershop.line-scdn.net/stickershop/v1/sticker/'+stickerId+'/iPhone/sticker@2x.png'
    # animation
    # url='https://stickershop.line-scdn.net/stickershop/v1/sticker/'+stickerId+'/iPhone/sticker_animation@2x.png'
    # message sticker
    # url='https://stickershop.line-scdn.net/stickershop/v1/sticker/'+stickerId+'/iPhone/base/plus/sticker@2x.png'
    r=requests.get(url)
    with open('./public/allSticker/'+folderName+'/'+stickerId+'.png','wb') as f:
        f.write(r.content)