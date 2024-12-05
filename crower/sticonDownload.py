import requests
import os

folderName='Something small and cute'
sticonId='6319855a83603436e7d1951d'
startId=1
endId=40

os.makedirs('./'+folderName+'/',exist_ok=True)

for stickerId in range(startId,endId):
    stickerId=str(stickerId)
    url='https://stickershop.line-scdn.net/sticonshop/v1/sticon/'+sticonId+'/iPhone/'+stickerId.zfill(3)+'.png'
    r=requests.get(url)
    with open('./'+folderName+'/'+stickerId+'.png','wb') as f:
        f.write(r.content)