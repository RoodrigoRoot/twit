import pytest
from tweets.models import Tweet
from django.urls import reverse

TWEET_CREATE_URL = reverse('tweets:create')
TWEET_LIST_URL = reverse('tweets:list')


@pytest.mark.django_db
def tests_create_tweet(user_factory, client):
    """Test that create a tweet succesful"""
    user = user_factory.create()
    payload = {"body": "Probando twitt4er", 'user': user.id}
    client.force_login(user)
    r = client.post(TWEET_CREATE_URL, payload)
    tweet = Tweet.objects.last()

    assert r.status_code == 201
    assert tweet.body == payload['body']


@pytest.mark.django_db
def tests_create_tweet_missing_body(user_factory, client):
    """Test that create a tweet without body filed fail"""
    user = user_factory.create()
    payload = {"body": "", 'user': user.id}
    client.force_login(user)
    r = client.post(TWEET_CREATE_URL, payload)
    response = r.json()

    assert r.status_code == 400
    assert 'message' in response.keys()


@pytest.mark.django_db
def tests_tweet_list(client, user_factory):
    """Test get a list oif tweets"""
    user = user_factory.create()
    client.force_login(user)
    r = client.get(TWEET_LIST_URL)
    response = r.json()

    assert r.status_code == 200
    assert response is not None
    assert type(response) == list
