#!/usr/bin/python3
import json
import requests
from sys import argv
from time import sleep


# converts dict to json
def to_json_string(list_dictionaries):
    """ converts dict to json """
    if list_dictionaries is None or list_dictionaries == []:
        return "[]"
    return json.dumps(list_dictionaries)


# saves json to json file
def save_to_file(LO_dict, name):
    """ write into a .json file """
    with open(name + ".json", "w") as f:
        f.write(to_json_string(LO_dict))

if __name__ == "__main__":
    usr_data = {}

    base_url = "https://jsonplaceholder.typicode.com/"

    url = "{}{}".format(base_url, "users")
    response = requests.get(url)
    users = response.json()
    ids = [x["id"] for x in users]
    for _id in ids:
        sleep(1)
        user_url = "{}users/{}".format(base_url, _id)
        tasks_url = "{}todos?userId={}".format(base_url, _id)

        response = requests.get(user_url)
        use_info = response.json()
        user_name = use_info.get("username")

        res = requests.get(tasks_url)
        tasks = res.json()

        _data = []
        for task in tasks:
            users_info = {"task": task.get("title"),
                          "completed": task.get("completed"),
                          "username": user_name}
            _data.append(users_info)

        usr_data[_id] = _data

    save_to_file(usr_data, "todo_all_employees")
