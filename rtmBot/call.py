#C:\Users\han\AppData\Local\Programs\Python\Python37-32\Scripts
import requests, json
import time
import zulip
import os
import datetime
import izyrtm_prop

filePath = os.getcwd()+'/snapshot/'

def getSessionId():

    loginParams = {'user': izyrtm_prop.apm_id, 'password':izyrtm_prop.apm_pw}
    loginHeader = {'Content-Type':'application/json'}
    loginUrl = izyrtm_prop.apm_url+'/login'

    print('1_'+loginUrl+' / '+izyrtm_prop.apm_id+' / '+izyrtm_prop.apm_pw)
    response = requests.post(url=loginUrl, headers=loginHeader, data=json.dumps(loginParams), verify=False)
    #print(response.json())
    #print(response.headers)
    print('1_')
    print(response.content)
    cookieValue = response.cookies.get('grafana_session')
    return cookieValue

def getSnapShot(sessionId, panelId, startDate, endDate):
    
    if startDate is '':
        endDate = datetime.datetime.now()
        endDateMil = str(int(endDate.timestamp()*1000))
        startDate = endDate - datetime.timedelta(hours = 3)
        startDateMil = str(int(startDate.timestamp()*1000))
    else:
        startDateMil = startDate
        endDateMil = endDate

    snapShotUrl = izyrtm_prop.apm_url+'/render/dashboard-solo/db/docker-and-system-monitoring?orgId=1&panelId='+panelId+'&from='+startDateMil+'&to='+endDateMil+'&width=1000&height=500'
    snapShotCookies = {'grafana_session': sessionId}
    #snapShotHeader = {'Content-Type':'application/json'}

    #snapShotParams = 'orgId=1&panelId=8&from=1568985607884&to=1569072007884&width=1000&height=500'

    response = requests.get(url=snapShotUrl, cookies=snapShotCookies, verify=False)
    print('2_'+str(sessionId))
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
    response = getSnapShot(sessionId, '8', '','')

    timestamp = int(time.time()*1000.0)
    fileName = str(timestamp)+'.png'
    saveFile(fileName, response)
    uploadedFileUri = uploadFile(fileName)
