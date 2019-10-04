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

#p = pprint.PrettyPrinter()

bName = ''
bSite = izyrtm_prop.domain
bEmail = ''
bApiKey = ''

class rtmBot(object):

    def __init__(self):
        print("done init1 -> "+str(bName)+' / '+bSite+' / '+bEmail+' / '+bApiKey)
        self.client = zulip.Client(site=bSite, email=bEmail, api_key=bApiKey)
        self.subscribe_all()

        print("done init2 -> "+str(bName)+' / '+bSite+' / '+bEmail+' / '+bApiKey)
        
    def subscribe_all(self):
        json = self.client.get_streams()["streams"]
        streams = [{"name": stream["name"]} for stream in json]
        self.client.add_subscriptions(streams)

    def process(self, msg):
        content = msg["content"].split()
        sender_email = msg["sender_email"]
        ttype = msg["type"]
        stream_name = msg['display_recipient']
        stream_topic = msg['subject']

        print(content)

        if sender_email == bEmail:
            return

        print("Sucessfully heard. / "+bName)

        if content[0].lower() == bName or content[0] == "@**"+bName+"**":
            if content[1] == "snapshot" :
                sessionId = call.getSessionId()

                panelId = '8' #default
                title = '컨테이너별 네트워크 트래픽'
                if content[2] is not None and content[2] == 'mem' :
                    panelId = '20'
                    title = '메모리 사용량'
                elif content[2] is not None and content[2] == 'network' :
                    panelId = '8'
                    title = '컨테이너별 네트워크 트래픽'
                elif content[2] is not None and content[2] == 'ccpu' or  content[2] == 'cpu':
                    panelId = '1'
                    title = '컨테이너별 CPU 사용량'
                elif content[2] is not None and content[2] == 'cmem' :
                    panelId = '10'
                    title = '컨테이너별 메모리 사용량'
               
                now = time.gmtime(time.time())
                now.tm_year, now.tm_mon, now.tm_mday
                response = izyrtm_call.getSnapShot(sessionId, panelId, '', '')

                timestamp = int(time.time()*1000.0)
                fileName = str(timestamp)+'.png'
                izyrtm_call.saveFile(fileName, response)
                uploadedFileUri = izyrtm_call.uploadFile(fileName, bSite, bEmail, bApiKey)
                
                self.client.send_message({
                    "type": "stream",
                    "subject": msg["subject"],
                    "to": msg["display_recipient"],
                    #"content": "[zulip-org-logo.png](https://monbot.hopto.org/user_uploads/3/4a/2NXyjQ72gL_UNc_3Lf4MrF4C/OUTPUT.png)"
                    "content": "["+title+"]("+izyrtm_prop.domain+uploadedFileUri+")"
                    })

            else:
                self.client.send_message({
                    "type": "stream",
                    "subject": msg["subject"],
                    "to": msg["display_recipient"],
                    "content": content[1]
                    })

        elif "rtm" in content and content[0] != "rtm":
                self.client.send_message({
                    "type": "stream",
                    "subject": msg["subject"],
                    "to": msg["display_recipient"],
                    "content": "Hey there! :blush:"
                    })
        elif "출첵" in content :
                self.client.send_message({
                    "type": "stream",
                    "subject": msg["subject"],
                    "to": msg["display_recipient"],
                    "content": "Hey! :blush:"
                    })
        else:
            return

def main():
    bot = rtmBot()
    bot.client.call_on_each_message(bot.process)
    
if __name__ == "__main__":
    if len(sys.argv) is not 4:
        print('check args')
        sys.exit(0)
    
    bName   = sys.argv[1]
    bApiKey = sys.argv[2]
    bEmail  = sys.argv[3]
    

    try:
        main()
    except KeyboardInterrupt:
        print("Thanks for using izyRtm Bot. Bye!")
        sys.exit(0)
