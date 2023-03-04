import requests
import os

startId=571838982
endId=571839021
folderName='ㄇㄚˊ幾兔ー豐富表情篇'

os.makedirs('./'+folderName+'/',exist_ok=True)

for stickerId in range(startId,endId):
    stickerId=str(stickerId)
    url='https://stickershop.line-scdn.net/stickershop/v1/sticker/'+stickerId+'/android/sticker.png'
    r=requests.get(url)
    with open('./'+folderName+'/'+stickerId+'.png','wb') as f:
        f.write(r.content)