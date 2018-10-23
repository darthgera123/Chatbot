import json
import requests

TOKEN = ""
URL = "https://api.telegram.org/bot{}/".format(TOKEN)

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content

def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js

def get_updates():
    url = URL+"getUpdates"
    content = get_json_from_url(url)
    return content

def getLastChat(content):
    text = content['result'][-1]['message']['text']
    id = content['result'][-1]['message']['chat']['id']
    return (text,id)

def sendMessage(text,chat_id):
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)

content = get_updates()
text , chat_id = getLastChat(content)
sendMessage("python rocks",chat_id)
