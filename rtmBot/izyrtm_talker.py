import pprint
import zulip
import sys
import re
import json
import httplib2
import os
import izyrtm_call
import time
import datetime
import izyrtm_prop
import sys

bName = ''
bSite = izyrtm_prop.domain
bEmail = ''
bApiKey = ''



class rtmBot(object):

    def __init__(self):
        self.client = zulip.Client(site=bSite, email=bEmail, api_key=bApiKey)
        #self.subscribe_all()

    def subscribe_all(self):
        json = self.client.get_streams()["streams"]
        streams = [{"name": stream["name"]} for stream in json]
        self.client.add_subscriptions(streams)

def main(subject, to, content):
    bot = rtmBot()
    bot.client.send_message({
                    "type": "stream",
                    "subject": subject,
                    #"topic": topic,
                    "to": to,
                    "content": content
                    })
    
if __name__ == "__main__":
    bSite = izyrtm_prop.domain
    bEmail = 'izyrtm-bot@monbot.hopto.org'
    bApiKey = 'SDTqdpwAdJobKlQbqSy1Bxz5F3xUwxxm'

    try:

        boo = False
        if boo is True:
            main('error상황창_20191005', 'general', 'izyrtm 관련인들 초대합니다.')
        else:
            bot = rtmBot()
            sessionId = izyrtm_call.getSessionId()

            panelId = '8' #default
            title = '컨테이너별 네트워크 트래픽'
           
            #panelId = '1'
            #title = '컨테이너별 CPU 사용량'
           
            now = time.gmtime(time.time())
            now.tm_year, now.tm_mon, now.tm_mday
            response = izyrtm_call.getSnapShot(sessionId, panelId, '', '')

            timestamp = int(time.time()*1000.0)
            fileName = str(timestamp)+'.png'
            izyrtm_call.saveFile(fileName, response)
            uploadedFileUri = izyrtm_call.uploadFile(fileName, bSite, bEmail, bApiKey)
            
            bot.client.send_message({
                "type": "stream",
                "subject": 'error상황창_20191005',
                "to": 'general',
                
                "content": "["+title+"]("+izyrtm_prop.domain+uploadedFileUri+")"
                })
                
    except KeyboardInterrupt:
        print("Thanks for using izyRtm Bot. Bye!")
        sys.exit(0)
