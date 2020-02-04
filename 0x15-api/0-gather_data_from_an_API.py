#!/usr/bin/python3
import requests
from sys import argv


if __name__ == "__main__":
    _id = argv[1]

    base_url = "https://jsonplaceholder.typicode.com/"
    user_url = "{}users/{}".format(base_url, _id)
    tasks_url = "{}todos?userId={}".format(base_url, _id)

    response = requests.get(user_url)
    use_info = response.json()
    name = use_info["name"]

    res = requests.get(tasks_url)
    tasks = res.json()

    done_tasks = 0
    total_tasks = 0
    completed_titles = []
    for task in tasks:
        if task["completed"]:
            done_tasks += 1
            completed_titles.append(task["title"])
        total_tasks += 1

    print("Employee {} ".format(name), end="")
    print("is done with tasks({}/{}):".format(done_tasks, total_tasks))
    for title in completed_titles:
        print("\t {}".format(title))
