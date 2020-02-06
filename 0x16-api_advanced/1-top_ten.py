#!/usr/bin/python3
""" querry reddit api for subreddit info"""
import requests
import requests.auth


def top_ten(subreddit):
    """ querry reddit api"""
    sub = subreddit
    subreddit = "/r/{}/hot".format(sub)
    temp = "HolbertonPass845"

    secret = "Z4Sa9bA6RRE44qDyhHQiTlW1gd0"
    client_id = "hy4KvoK0W2iDvw"
    usr_name = "jgadelugo"

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

    headers = {"Authorization": "{} {}".format(token_type, access_token),
               "User-Agent": "ChangeMeClient/0.1 by {}".format(usr_name)}

    param = {"limit": 10}

    query = "https://oauth.reddit.com{}".format(subreddit)
    res = requests.get(query, headers=headers, params=param)

    status = res.status_code

    if (status != 200):
        print("None")
    else:
        data = res.json()
        posts = data["data"]['children']
        for post in posts:
            print(post['data']['title'])
