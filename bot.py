import sys, os, zulip
sys.path.insert(0,os.getcwd())

from wit import Wit
from typing import Any, Dict

#Client = Wit(Insert key)

class KumbhBot(object):
    def usage(self):
        return "Build withZulip chat api and python, KumbhBot works as a savior for people visiting The Popular Ritual People Gathering KUMBH"
    def handle_message(self,message: Dict[str,str],bot_handler:Any) -> None:
        ans=[]
        question=""
        print(message["content"])
        if message["content"] == "" or message["content"] == "help":
            ans.append(utils.HELP_MESSAGE)
        data=message["content"].split()
        if(data[0] != "Kumbh"):
                data.insert(0,"Kumbh")
                message["content"] = "Kumbh " + message["content"]
                
            
        if question == "weather":
            ans.append(weather.forecast_weather())
        elif question == "trainEnquiry":
                TrainNo = data[2::]
                ans.append(train.train_enquiry(TrainNo))
        elif question == "findRoute":
            TrainNo = data[2::]
            ans.append(train.train_route(TrainNo))
        elif question == "liveStation":
            place = data[2::]
            ans.append(train.live_station(place))
        elif question == "bath":
            ans.append(events.bath())
        elif question == "hospital":
            ans.append(emergency.hospital())
        elif question == "restaurant":
            ans.append(emergency.restaurant())
        elif question == "emergencyContact":
            ans.append(emergency.contacts())
        elif question == "help":
            ans.append(utils.HELP_MESSAGE)
        elif question == "trainTo":
            first = data[2::]
            ans.append(train.train_between(first))
        else:
            temp = data[1::]
            temp = " ".join(dataTemp)
            print(temp)
            witAnalysis = client.message(temp)
            print(witAnalysis)
            temp = witAnalysis['entities']
            if temp.__len__() == 0:
            	ans.append('Sorry :( I could not understatnd what you want to say.')
            	ans.append(' Try "@Kumbh help" to get detailed help ')
            else:
            	trait = witAnalysis['entities']['intent'][0]['value']
            	if   trait == "hello":
            	        ans.append("Hello I am KumbhBot nice to meet you !!!!Hope you are enjoying Kumbh to the fullest  :)")
            	elif trait == "bye":
            	        ans.append("Good bye see you soon :)")
        final_reply=""
        for index, result in enumerate(ans, 1):
                final_reply += ((str(index)) if len(ans) > 1 else '') + result + '\n'

        bot_handler.send_reply(message, final_reply)
    


                
        

    
