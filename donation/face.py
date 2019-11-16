import facebook
import json
import requests
from json import load
from urllib.request import urlopen

def facebookview():
    token='EAALOtHuxZAWUBAHyNRy0sGk95VxqliMEYZCJCKMe7zUrlK9HbOZAwpCwqsKc8zpXcJjPU2ZAcrJBPJldEBpbGG2kcZBdv3EbDNTIzTBVzO0mTxtpMiVjZAlqHqSr1TbCwtjZCBXFWPZCUrV67eePl8Rbj7F9uz0baviPdEz98bYoIxWtys5ltLKZC8romZBoEiUEFoWObAMEbdWmGtkS6T6kDC'
    #facebook.GraphAPI(access_token=token)
    
    graph = facebook.GraphAPI(token)
    fields = ['posts','id']
    fields = ','.join(fields)
    page = graph.get_object('107316914058945',fields = fields)
    print(json.dumps(page,indent=4))
    data = json.dumps(page)
    #print(data)
    #faceb = OpenFacebook(access_token=token)
    #faceb.set('me/feed', message='Test1',url='http://www.something')
   
def socialview():
    url="https://graph.facebook.com/v5.0/107316914058945?fields=posts.limit(20)%7Bmessage%2Cfrom%2Cadmin_creator%2Clikes.limit(30)%2Cfull_picture%7D%2Cevents.limit(10)%7Bowner%2Cdescription%2Cstart_time%7D&access_token=EAALOtHuxZAWUBAP51gsl4HZC7oBhEvObVi2IufcuBcdfVGEEBWiPAyTOIlqa7ZAFZCLnOChoyrngn2DB3kQv3TqZABZBxTTCkP1YxqLFLUCRXIUHQdQN72GgEfwLulFqJlgNOwbA4hxx9ZAGnO9YjulKh5ALasfqyxWJN7J678KB6qNeksz42H4ZBgq6bLg6T7r2Ws1lCbSJBAZDZD"
    response=urlopen(url)
    json_text = load(response)
    
    feed_messages=list()
    feed_pictures=list()
    

    event_owner=list()
    event_description=list()
    event_start=list()

    for info in json_text["posts"]["data"]:
        mess=info.get('message', 'null')
        pics=info.get('full_picture','null')
        likes=info.get('likes','null')
        feed_messages.append(mess)
        feed_pictures.append(pics)
        
    
   
        
    
    for info in json_text["events"]["data"]:
        mess=info.get('description', 'null')
        owner=info.get('name', 'null')
        start=info.get('start_time','null')
        event_description.append(mess)
        event_owner.append(owner)
        event_start.append(pics)
        
   
    #print(feed_pictures)
    #print(event_description)
    #print(event_owner)
    #print(event_start)
    


socialview()
