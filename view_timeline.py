from datetime import datetime
from helper_functions import add_members, create_tweepy_object

# Target twitter account
twitter_handle = ""  # Ex: "github" (which is @github)
timeline_date = datetime.today().strftime('%m/%d/%y')

if __name__ == "__main__":
    # Create twitter api connection
    api = create_tweepy_object()

    # Get target twitter handle's user object.
    twitter_account = api.get_user(twitter_handle)

    # Create list, and save it's ID
    list_id = \
        getattr(
            api.create_list((twitter_handle + "'s " + " timeline"), "public")
            , 'id')

    # Get twitter friends account ID's
    twitter_account_friends = api.friends_ids(twitter_handle)

    # Add friends to timeline list
    add_members(api, list_id, twitter_account_friends)

    # Return list url for viewing the timeline
    print('You may view @' + twitter_handle + "'s timeline at " +
          'https://twitter.com/i/lists/' + str(list_id))
