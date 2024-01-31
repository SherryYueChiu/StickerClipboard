import requests
import os

startId=643889462
endId=643889501
folderName='ㄇㄚˊ幾兔－追星篇'

os.makedirs('./allSticker/'+folderName+'/',exist_ok=True)

for stickerId in range(startId,endId):
    stickerId=str(stickerId)
    url='https://stickershop.line-scdn.net/stickershop/v1/sticker/'+stickerId+'/android/sticker.png'
    r=requests.get(url)
    with open('./allSticker/'+folderName+'/'+stickerId+'.png','wb') as f:
        f.write(r.content)