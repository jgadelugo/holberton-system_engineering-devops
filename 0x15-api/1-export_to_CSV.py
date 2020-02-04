#!/usr/bin/python3
from csv import DictWriter, QUOTE_ALL
import requests
from sys import argv


# creates CSV file - takes in dictionary
def write_to_csv(_data, _id):
    """takes in data as a dictionary, and the id for name """
    with open("{}.csv".format(_id), "w") as file:
        headers = ["USER_ID", "USERNAME",
                   "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        csv_writer = DictWriter(file, fieldnames=headers, quoting=QUOTE_ALL)
        for apt in _data:
            csv_writer.writerow(apt)
    return

if __name__ == "__main__":
    _id = argv[1]

    base_url = "https://jsonplaceholder.typicode.com/"
    user_url = "{}users/{}".format(base_url, _id)
    tasks_url = "{}todos?userId={}".format(base_url, _id)

    response = requests.get(user_url)
    use_info = response.json()
    user_name = use_info.get("username")

    res = requests.get(tasks_url)
    tasks = res.json()

    _data = []
    for task in tasks:
        users_info = {"USER_ID": _id,
                      "USERNAME": user_name,
                      "TASK_COMPLETED_STATUS": task.get("completed"),
                      "TASK_TITLE": task.get("title")}
        _data.append(users_info)

    write_to_csv(_data, _id)
