# izyrtm
docker-compose up -d


# rm all
docker-compose rm -s

# bot run
nohup python3 izyrtm.py &

#check process (example)
zulip@hanhost:~/izyrtm/rtmBot$ ps -ef | grep izyrtm

zulip    24059     1  0 00:55 pts/2    00:00:00 python3 /home/zulip/izyrtm/rtmBot/izyrtm_node.py 2 0erVHGVEPN9diAkCRQ2o5z4YShIAmcMo noti-bot@monbot.hopto.org

zulip    24061     1  0 00:55 pts/2    00:00:00 python3 /home/zulip/izyrtm/rtmBot/izyrtm_node.py 4 GEfnvBUnJ4s17aUz7IrrhYpZmGkTl1xJ hi-bot@monbot.hopto.org

zulip    24063     1  0 00:55 pts/2    00:00:00 python3 /home/zulip/izyrtm/rtmBot/izyrtm_node.py 5 SDTqdpwAdJobKlQbqSy1Bxz5F3xUwxxm izyrtm-bot@monbot.hopto.org
