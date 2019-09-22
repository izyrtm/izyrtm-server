#C:\Users\han\AppData\Local\Programs\Python\Python37-32\Scripts
import requests, json
import time
import zulip
import os

filePath = os.getcwd()+'/snapshot/'

def getSessionId():

    loginParams = {'user': 'admin', 'password':'New1234!'}
    loginHeader = {'Content-Type':'application/json'}
    loginUrl = 'https://monbot.hopto.org:3000/login'

    response = requests.post(url=loginUrl, headers=loginHeader, data=json.dumps(loginParams), verify=False)
    #print(response.json())
    #print(response.headers)
    print('1_')
    print(response.content)
    cookieValue = response.cookies.get('grafana_session')
    return cookieValue

def getSnapShot(sessionId):
    snapShotUrl = 'https://monbot.hopto.org:3000/render/dashboard-solo/db/docker-and-system-monitoring?orgId=1&panelId=8&from=1568985607884&to=1569072007884&width=1000&height=500'
    snapShotCookies = {'grafana_session': sessionId}
    #snapShotHeader = {'Content-Type':'application/json'}

    #snapShotParams = 'orgId=1&panelId=8&from=1568985607884&to=1569072007884&width=1000&height=500'

    response = requests.get(url=snapShotUrl, cookies=snapShotCookies, verify=False)
    print('2_')
    #print(response.content)
    return response

def saveFile(fileName, response):
    if not(os.path.isdir(filePath)):
        os.makedirs(os.path.join(filePath))

    open(filePath+fileName, 'wb').write(response.content)

def uploadFile(fileName):
    client = zulip.Client(config_file="~/.zuliprc")

    # Upload a file
    path_to_file = filePath + fileName
    with open(path_to_file, 'rb') as fp:
        result = client.call_endpoint(
            'user_uploads',
            method='POST',
            files=[fp]
        )
    #print(result)
    return getZulipFilePath(result)

def getZulipFilePath(result):
    data = result.get('uri')
    return data

if __name__ == '__main__':
    sessionId = getSessionId()
    response = getSnapShot(sessionId)

    timestamp = int(time.time()*1000.0)
    fileName = str(timestamp)+'.png'
    saveFile(fileName, response)
    uploadedFileUri = uploadFile(fileName)
