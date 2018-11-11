import tweepy as tw
from time import sleep

# copy all this into your python IDE, PyCharm, or whatever you have. 
# Moreover create a text file called ID_STORAGE.txt and save this number there 1061733021919989760 [random twitter tweet id]
# if you are using linux/ ubuntu create a vim my_twitter_bot.py and vim ID_STORAGE.txt and insert it all


# Here go your open browser where you had Keys and tokens:

# from 'Consumer API keys' copy inside of single quotes:

CONSUMER_KEY =''   # API key
CONSUMER_SECRET='' #API secret key

ACCESS_KEY=''      # Access token
ACCESS_SECRET =''  # Access token secret

# here you are creating puppeteer to your puppet account
auth = tw.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api =tw.API(auth)



FILE_NAME ='ID_STORAGE.txt'  # keeping your file name understandable


def retrieve_last_seen(file_name):       # this function to get tweet ids to which you've replied so far
    f_read = open(file_name, 'r')        # allowing file to be just read and nothing else
    lastSeen =int(f_read.read().strip()) # removes spaces and turn the text into a huge integer
    f_read.close()
    return lastSeen


def store_last_seen(last, file_name): # this function to save tweet ids to which you just replied
    f_write = open(file_name, 'w')    #just write
    f_write.write(str(last))          #turn the integer you passed to string and add to the file
    f_write.close()
    return

last_seen_id = retrieve_last_seen(FILE_NAME)    # it will go to the file take all 
mentions = api.mentions_timeline(last_seen_id, tweet_mode='extended')

def reply_to_tweets():
    print("Getting tweets and replying to tweets...")

    LastSID =retrieve_last_seen(FILE_NAME)
    # mentions saves whatever is said in your time line on twitter
    mentions =api.mentions_timeline(LastSID, tweet_mode ='extended')

    for i in reversed(mentions):         # reversed to reverse the timeline to begin replying from the first tweet
        last = i.id                      
        store_last_seen(last, FILE_NAME) # check if you've already replied to it
        if '#sad' in i.full_text.lower():# if the #sad was used in tweet directed to you
            api.update_status('@'+i.user.screen_name +" Don't sweat it, it's gonna be fine my friend",
                              i.id)
                                         # reply with '@'+ their name + your response

while True:             # runs until you press stop or ctr+c
    reply_to_tweets()
    sleep(5)            #takes a brake for 5 seconds between tweets. (or increase and decrese it)
                        #P.S. Twitter does not allow barrage of tweets from one account in short period of time(They may block you)
                        # Therefore, you should probably increase brake time
