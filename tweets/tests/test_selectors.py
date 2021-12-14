import pytest
from tweets.selectors import tweet_get, tweet_list
from tweets.services import tweet_create
from uuid import UUID


@pytest.mark.django_db
def tests_tweet_get(user_factory):
    """Test get a tweet succesful"""
    user = user_factory.create()
    res = tweet_create(body='tests', user_id=user.id)
    tweet = res["tweet"]
    res = tweet_get(tweet.id)
    assert res is not None
    assert type(res.id) == int


@pytest.mark.django_db
def tests_tweet_list(user_factory):
    """Test get a list of tweet succesful"""
    user = user_factory.create()
    tweet_create(body='tests', user_id=user.id)
    tweets = tweet_list()

    assert tweets is not None

