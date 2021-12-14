from tweets.models import Tweet
from typing import List


def tweet_get(tweet_id: int) -> Tweet:
    try:
        tweet = Tweet.objects.get(id=tweet_id)
        return tweet
    except Tweet.DoesNotExist as dne:
        print(dne)


def tweet_list() -> List[Tweet]:
    tweets = Tweet.objects.all().order_by('created_at')
    return tweets
