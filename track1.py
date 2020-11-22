import tweepy
import config
import data
import time

auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)

api = tweepy.API(auth)

pollutionData = dict([("Ahmedabad",data.Ahmedabad),("Bengaluru",data.Bengaluru),("Gaya",data.Gaya),("Jaipur",data.Jaipur),("Durgapur",data.Durgapur),("Ghaziabad",data.Ghaziabad),("Mumbai",data.Mumbai)])
sortedData = sorted(pollutionData.items(), key=lambda x: x[1])    
sortedData.reverse()

def comment(idx):
   if(idx>=0 and idx<=50):
      return ("Minimal impact! People staying here have taken measures to decrease air pollution.")
   elif(idx>=51 and idx<=100):
      return ("Minor breathing discomfort to sensitive people")
   elif(idx>=101 and idx<=200):
      return ("Breathing discomfort to the people with lungs, asthma and heart diseases!")
   elif(idx>=201 and idx<=300):
      return ("Breathing discomfort to most people on prolonged exposure! Save me from toxic gases!")
   
# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

# user = api.get_user('abhi211199')
# print(user.screen_name)
# print(user.followers_count)
# for friend in user.friends():
#    print(friend.screen_name)


# user = api.retweets_of_me(count=1)
# for friend in user:
#    print(friend)
# api.update_status()
# user=api.mentions_timeline()
# # user=api.list_direct_messages()
# print(user[1])
# for friend in user:
#    print(friend)


# api.update_status("This is a tree speaking from " + sortedData[0][0] + ". The AQI for this place is " +  sortedData[0][1] + "." + comment(sortedData[0][1]) + ". ɴᴏᴛᴇ: ᴛʜɪꜱ ɪꜱ ᴀ ᴛᴡᴇᴇᴛ ʙʏ ᴀ ʙᴏᴛ ʙᴜɪʟᴛ ᴅᴜʀɪɴɢ #ᴄᴏᴅᴇᴄʜᴇʟʟᴀ ʜᴀᴄᴋᴀᴛʜᴏɴ! ʙᴜɪʟᴛ ᴏɴʟʏ ꜰᴏʀ ᴛᴇꜱᴛɪɴɢ ᴘᴜʀᴘᴏꜱᴇꜱ!" )
# str1 = "This is a tree speaking from " + str(sortedData[0][0]) + ".\nThe AQI for this place is " +  str(sortedData[0][1]) + ". \n" + comment(sortedData[0][1]) + ".\nᴛʜɪꜱ ɪꜱ ᴀ ᴛᴡᴇᴇᴛ ʙʏ ᴀ ʙᴏᴛ ʙᴜɪʟᴛ ᴅᴜʀɪɴɢ #ᴄᴏᴅᴇᴄʜᴇʟʟᴀ! ʙᴜɪʟᴛ ᴏɴʟʏ ꜰᴏʀ ᴛᴇꜱᴛɪɴɢ ᴘᴜʀᴘᴏꜱᴇꜱ!"
# print(str1)
# api.update_status(str1)

# time.sleep(2)

# global k
k=1
from itertools import count
iid = count(1)


class MyStreamListener(tweepy.StreamListener):
    # global k
    # k=1
    def on_status(self, stat):
      k=next(iid)
      print(stat.id)
      api.update_status(in_reply_to_status_id=stat.id,status="This is a tree speaking from " + str(sortedData[k][0]) + ".\nThe AQI for this place is " +  str(sortedData[k][1]) + ". \n" + comment(sortedData[k][1]) + ".\nᴛʜɪꜱ ɪꜱ ᴀ ᴛᴡᴇᴇᴛ ʙʏ ᴀ ʙᴏᴛ ʙᴜɪʟᴛ ᴅᴜʀɪɴɢ #CODECHELLA! ʙᴜɪʟᴛ ᴏɴʟʏ ꜰᴏʀ ᴛᴇꜱᴛɪɴɢ ᴘᴜʀᴘᴏꜱᴇꜱ!")
      k=k+1
      

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

myStream.filter(follow=["2556511056"])


# print(next(iid))
# print(next(iid))
