import tweepy


consumer_key = 'some key'
consumer_secret = 'some secret'
access_token = 'some token'
access_secret = 'some token secret'

auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

# for the query syntax see Twitter API documentation: https://dev.twitter.com/rest/public/search
# api search query syntax:  https://dev.twitter.com/rest/reference/get/search/tweets

tweets = api.search(q='django python', count=100)

# query parameters
# q (required), getcode, lang, locale, result_type, count (default 15), until, since_id, max_id, include_entities

# results are returned as a list
# fields in the returned list is defined by Twitter API: https://dev.twitter.com/overview/api/tweets
# https://dev.twitter.com/overview/api/tweets
# contributors
# coordinates               geographic location
# created_at                UTC time
# current_user_retweet
# entities
# favorite_count            number of likes
# favorited                 boolean
# filter_level              filter level parameter, 'none', 'low' or 'medium'
# id                        unique identifier for each tweet
# id_str                    string representation of id
# in_reply_to_screen_name
# in_reply_to_status_id
# in_reply_to_status_id_str
# in_reply_to_user_id
# in_reply_to_user_id-str
# lang                      language
# place                     place name and coordinates
# possibly_sensitive
# quoted_status_id
# quoted_status_id_str
# quoted_status
# scopes
# retweet_count             retweet count
# retweeted                 boolean
# retweeted_status
# source                    source of the tweet as HTML
# text                      tweet
# truncated                 boolean, if the text is truncated
# user                      Users user who posted the tweet. Users has its attributes.
# withheld_copyright        boolean, if the content is withdrawn due to DMCA complaint
# withheld_in_countries     two-letter code of countries the tweet is withheld from
# withheld_scope            when present whether the withheld content is 'status' or 'user'



for t in tweets:
    print(t.created_at, t.user.name, t.text, '\n')
    #print(t.coordinates)