import tweepy

consumer_key = 'some key'
consumer_secret = 'some secret'
access_token = 'some token'
access_secret = 'some token secret'

auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

tweets = api.search(q='faridyu')
user = api.get_user('faridyu')

print(user.screen_name)
print(user.followers_count)
for friend in user.friends():
    print(friend.screen_name)