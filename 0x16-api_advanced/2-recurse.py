#!/usr/bin/python3
""" querry reddit api for subreddit info
"""
import requests
import requests.auth
from time import sleep


def authenticate():
    """ authenticate function
    doesnt take parameters returns token_type and access_token
    """
    usr_name = "jgadelugo"
    temp = "HolbertonPass845"

    secret = "Z4Sa9bA6RRE44qDyhHQiTlW1gd0"
    client_id = "hy4KvoK0W2iDvw"

    client_auth = requests.auth.HTTPBasicAuth(client_id, secret)
    post_data = {"grant_type": "password",
                 "username": usr_name,
                 "password": temp}

    headers = {"User-Agent": "ChangeMeClient/0.1 by {}".format(usr_name)}
    response = requests.post("https://www.reddit.com/api/v1/access_token",
                             auth=client_auth, data=post_data, headers=headers)
    auth_json = response.json()

    token_type = auth_json['token_type']
    access_token = auth_json['access_token']

    return (token_type, access_token)


def recurse(subreddit, hot_list=[], after=[], t_type=None, a_token=None):
    """ querry reddit api for hot post
    recursively get all hot post from subreddit
    """
    sub = subreddit
    subreddit = "/r/{}/hot".format(sub)
    usr_name = "jgadelugo"

    if len(after) == 0:
        t_type, a_token = authenticate()

    headers = {"Authorization": "{} {}".format(t_type, a_token),
               "User-Agent": "ChangeMeClient/0.1 by {}".format(usr_name)}
    if len(after) != 0:
        param = {"limit": 100, "after": after[-1]}
    else:
        param = {"limit": 100}

    sleep(1)
    query = "https://oauth.reddit.com{}".format(subreddit)
    res = requests.get(query, headers=headers, params=param)

    status = res.status_code

    if (status != 200):
        return None
    else:
        data = res.json()
        if data['data']['after'] in after:
            return hot_list
        after.append(data['data']['after'])
        posts = data["data"]['children']
        for post in posts:
            hot_list.append(post['data']['title'])

        return recurse(sub, hot_list, after, t_type, a_token)
