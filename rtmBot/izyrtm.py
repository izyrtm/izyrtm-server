import pprint
import zulip
import sys
import re
import json
import httplib2
import os
import call
import time

p = pprint.PrettyPrinter()
BOT_MAIL = "hi-bot@monbot.hopto.org"

class ZulipBot(object):
    def __init__(self):
        self.client = zulip.Client(site="https://monbot.hopto.org")
        self.subscribe_all()

        print("done init")
        
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

        if sender_email == BOT_MAIL:
            return

        print("Sucessfully heard.")

        if content[0].lower() == "rtm" or content[0] == "@**rtm**":
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
               
                response = call.getSnapShot(sessionId, panelId)

                timestamp = int(time.time()*1000.0)
                fileName = str(timestamp)+'.png'
                call.saveFile(fileName, response)
                uploadedFileUri = call.uploadFile(fileName)
                
                self.client.send_message({
                    "type": "stream",
                    "subject": msg["subject"],
                    "to": msg["display_recipient"],
                    #"content": "[zulip-org-logo.png](https://monbot.hopto.org/user_uploads/3/4a/2NXyjQ72gL_UNc_3Lf4MrF4C/OUTPUT.png)"
                    "content": "["+title+"](https://monbot.hopto.org"+uploadedFileUri+")"
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
        else:
            return

def main():
    bot = ZulipBot()
    bot.client.call_on_each_message(bot.process)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Thanks for using izyRtm Bot. Bye!")
        sys.exit(0)
