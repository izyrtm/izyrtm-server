import izyrtm_prop
import izyrtm_db
import subprocess
import os
import signal
import sys

def showList():
    for line in os.popen("ps ax | grep izyrtm_node | grep -v grep"):
        fields = line.split()
        print(fields)
        print('\n')

def stopAll():
    for line in os.popen("ps ax | grep izyrtm_node | grep -v grep"):
        fields = line.split()
        pid = fields[0]
        os.kill(int(pid), signal.SIGKILL)
    
def main():
    for line in os.popen("ps ax | grep izyrtm_node | grep -v grep"):
        fields = line.split()
        pid = fields[0]
        os.kill(int(pid), signal.SIGKILL)
        
    botList = izyrtm_db.getBotList()
    for i in botList:
        seqNo = i['seq_no']
        botToken = i['bot_token']
        useYn = i['use_yn']
        botEmail = i['bot_key']
        site = izyrtm_prop.domain
        
        if useYn is 'Y' :
            arg = 'nohup python3 '+os.getcwd()+'/izyrtm_node.py '+str(seqNo)+' '+botToken+' '+botEmail+' &'
            #proc = subprocess.Popen(['python', arg])
            #proc = subprocess.Popen(['C:/Users/han/AppData/Local/Programs/Python/Python37-32/python.exe', arg])

            subprocess.call(arg, shell=True)
            #subprocess.Popen(['nohup', arg], stdout=open('/dev/null', 'w'), stderr=open('logfile.log', 'a'), preexec_fn=os.setpgrp)
            #email = 'izyrtm-bot@monbot.hopto.org'
            #apiKey = 'GEfnvBUnJ4s17aUz7IrrhYpZmGkTl1xJ'
            #botName = 'rtm'

            #bot = izyrtm_bot.rtmBot(seqNo, site, botEmail, botToken)
            #bot.client.call_on_each_message(bot.process)
            print('run bot : '+str(seqNo)+' / '+site+' / '+botEmail+' / '+botToken)

        else :
            for line in os.popen("ps ax | grep " + botToken + " | grep -v grep"):
                fields = line.split()
                pid = fields[0]
                os.kill(int(pid), signal.SIGKILL)
            #seq_no,bot_key,bot_token,bot_type,bot_title,topic_name,user_list,use_yn,reg_dt,mod_dt
            #print(str(i['seq_no'])+' / '+str(i['bot_key'])+' / '+str(i['bot_token'])+' / '+str(i['bot_type'])+' / '+str(i['bot_title'])+' / '+str(i['topic_name'])+' / '+str(i['user_list'])+' / '+str(i['use_yn']))
            #print("\n")

if __name__ == "__main__":
    if len(sys.argv) is 2:
        if sys.argv[1] is 'stop':
            stopAll()
        elif sys.argv[1] is 'status':
            showList()
        else:
            main()
    else:
        main()
