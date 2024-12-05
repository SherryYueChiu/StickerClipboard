import requests
import os

startId=4873504
endId=4873543
folderName='Life of chicken and chicks2'

os.makedirs('./allSticker/'+folderName+'/',exist_ok=True)

for stickerId in range(startId,endId):
    stickerId=str(stickerId)
    # low resolution
    # url='https://stickershop.line-scdn.net/stickershop/v1/sticker/'+stickerId+'/android/sticker.png'
    # high resolution
    url='https://stickershop.line-scdn.net/stickershop/v1/sticker/'+stickerId+'/iPhone/sticker@2x.png'
    # animation
    # url='https://stickershop.line-scdn.net/stickershop/v1/sticker/'+stickerId+'/iPhone/sticker_animation@2x.png'
    r=requests.get(url)
    with open('./allSticker/'+folderName+'/'+stickerId+'.png','wb') as f:
        f.write(r.content)