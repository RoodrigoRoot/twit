from tweets.models import Tweet
from accounts.selectors import get_user_by_id


def tweet_create(body: str, user_id: int) -> Tweet:
    user = get_user_by_id(user_id)
    data = {}
    try:
        tweet = Tweet(body=body, user=user)
        tweet.full_clean()
        tweet.save()
        data = {"tweet": tweet, "results": True}
        return data
    except Exception as e:
        data = {"message": "The field body doesn't can't blank", "results": False}
        return data

