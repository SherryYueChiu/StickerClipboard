import requests
import os

folderName='cutekiwi move Emoji'
sticonId='65484c048e943e070d985dbe'
startId=1
endId=40

os.makedirs('./allSticker/'+folderName+'/',exist_ok=True)

for stickerId in range(startId,endId):
    stickerId=str(stickerId)
    # static
    # url='https://stickershop.line-scdn.net/sticonshop/v1/sticon/'+sticonId+'/iPhone/'+stickerId.zfill(3)+'.png'
    # animation
    url='https://stickershop.line-scdn.net/sticonshop/v1/sticon/'+sticonId+'/iPhone/'+stickerId.zfill(3)+'_animation.png'
    r=requests.get(url)
    with open('./allSticker/'+folderName+'/'+stickerId+'.png','wb') as f:
        f.write(r.content)