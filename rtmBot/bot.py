import pprint
import zulip
import sys
import re
import json
import httplib2
import os



p = pprint.PrettyPrinter()
BOT_MAIL = "hi-bot@monbot.hopto.org"

class ZulipBot(object):
	def __init__(self):
		self.client = zulip.Client(site="https://monbot.hopto.org")
		self.subscribe_all()
						
		print("done init")
		self.subkeys = ["translate", "hackernews", "hn", "hotel", "HN", "askme", "cricnews", "movie", "currency", "holiday", "lyrics"]

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
