import tweepy, os
from dotenv import load_dotenv
load_dotenv()

# Creates the twitter api connection and returns a tweepy
# object after it's been authenticated
def create_tweepy_object():
    # Note: You will need to apply for a twitter developer
    # account @https://developer.twitter.com/en to obtain these credentials
    auth = tweepy.OAuthHandler(os.getenv('CONSUMER_KEY'), os.getenv('CONSUMER_SECRET'))
    auth.set_access_token(os.getenv('ACCESS_TOKEN'), os.getenv('ACCESS_TOKEN_SECRET'))

    # Rate limit aware authentication
    api = tweepy.API(auth)

    # Validate Credentials
    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")

    # Return tweepy object
    return api


# Takes a list of member id's and adds them to a twitter list.
def add_members(twitter_api, list_id, friends_ids):
    # List holding members to be added to the twitter list
    members_list = []

    # Add each member into the list.
    for i, account_id in enumerate(friends_ids):
        # There is a limit of 5000 members on twitter lists.
        # So you need to stop adding past that.
        if i == 5000:
            members_list = []
            break
        # The add_list_members() method has a maximum of 100 users
        elif i % 100 == 0:
            if i != 0:
                twitter_api.add_list_members(list_id=list_id, user_id=members_list)
                members_list = []
            else:
                members_list.append(account_id)
        else:
            members_list.append(account_id)

    # Check to see if there are any friends left to add
    if len(members_list) > 0:
        twitter_api.add_list_members(list_id=list_id, user_id=members_list)

    return True


# Returns back a json object with the current accounts rate limits.
def check_rate_limits(twitter_api):
    return twitter_api.rate_limit_status()
