
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions



from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
# For youtube api for action_music_world
from googleapiclient.discovery import build
import requests
import random


# custom action for handling the music requests.
class ActionMusicWorld(Action):

    def name(self) -> Text:
        return "action_music_world"


    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: "DomainDict",) -> List[Dict[Text, Any]]:
        try:
            word = tracker.latest_message['text']
            api_key = ####################################
            youtube = build('youtube', 'v3', developerKey=api_key)
            # print(type(youtube))
            req = youtube.search().list(q=word, part='snippet', type='video')
            # print(type(req))
            print(word)
            res = req.execute()
            # print(res['items'])
            links = []
            for item in res['items']:
                # print(item['snippet']['title'])
                vid = item['id']['videoId']
                link = ("https://www.youtube.com/watch?v=" + vid)
                # print(link)
                links.append(link)

            l = len(links)

            if l >= 1:
                i = random.randint(0, l)
                Link = links[i]
                dispatcher.utter_message(template="utter_music", link=Link)

            else:
                Link = links
                dispatcher.utter_message(template="utter_except")
        except Exception as e:
            dispatcher.utter_message(template="utter_except")
            print(e)
        return[]


# custom action for handling the Twitter requests.
class ActionTwitterSearch(Action):

    def name(self) -> Text:
        return "action_twitter_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Twittering in!")

        return []















#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
