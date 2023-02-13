"""
    Consuming Twitter data
"""
# !pip install tweepy
import socket
import tweepy
from tt_secrets import BEARER_KEY

HOST = 'localhost'
PORT = 3001

s = socket.socket()

s.bind((HOST,PORT))
print(f'Waiting Connection -> PORT {PORT}')
s.listen(5)
con, adr = s.accept()
print('Request received from {adr}')
print(con)


KEYWORD = 'hogwarts legacy'

class GetTweets(tweepy.StreamingClient):
    """Extends another, but needed of some modifications

    Args:
        tweepy (lib): Dad class
    """
    def on_tweet(self, tweet):
        """Def to print tweet

        Args:
            tweet (json): Tweet json
        """
        print(tweet)
        print('-'*50)
        con.send(tweet.text.encode('utf-8','ignore'))
    
printer = GetTweets(BEARER_KEY)
printer.add_rules(tweepy.StreamRule(KEYWORD))
printer.filter()
con.close()
        