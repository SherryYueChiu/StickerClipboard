import requests
import os

folderName='貓貓蟲-咖波 動態表情貼'
sticonId='6124aa4ae72c607c18108562'
startId=1
endId=40

os.makedirs('./'+folderName+'/',exist_ok=True)

for stickerId in range(startId,endId):
    stickerId=str(stickerId)
    url='https://stickershop.line-scdn.net/sticonshop/v1/sticon/'+sticonId+'/iPhone/'+stickerId.zfill(3)+'.png'
    r=requests.get(url)
    with open('./'+folderName+'/'+stickerId+'.png','wb') as f:
        f.write(r.content)