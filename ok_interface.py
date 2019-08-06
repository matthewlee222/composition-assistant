import re
import webbrowser

import requests

from secrets import ACCESS_TOKEN


def get_backup_ids(file="raw_queue.txt", completed_file="completed"):
    with open(file, "r+") as f, open(completed_file) as g:
        text = f.read()
        ids = re.findall(r"/composition/(.+)\?", text)
        completed_ids = [id.strip() for id in g]
        ids = [id for id in ids if id not in completed_ids]
        f.seek(0)
        f.write(
            "\n".join(
                f"https://okpy.org/admin/composition/{id}?diff=full" for id in ids
            )
        )
        f.truncate()
        return ids


def get_backup_code(id):
    params = {"access_token": ACCESS_TOKEN}
    r = requests.get(f"https://okpy.org/api/v3/backups/{id}", params=params)
    messages = r.json()["data"]["messages"]
    out = None
    for message in messages:
        if "ants.py" in message["contents"]:
            if out is not None:
                raise Exception("Multiple ants.py found???")
            out = message["contents"]["ants.py"]

    if out is None:
        raise Exception("No ants.py found!!!")

    return out


def submit_comment(id, line, message):
    params = {"access_token": ACCESS_TOKEN}
    data = {"filename": "ants.py", "line": line, "message": message}
    r = requests.post(
        f"https://okpy.org/api/v3/backups/{id}/comment/", params=params, data=data
    )
    assert r.status_code == 200, "fail"


def submit_grade(id, score, message, completed="completed"):
    params = {"access_token": ACCESS_TOKEN}
    data = {"bid": id, "kind": "composition", "score": score, "message": message}
    r = requests.post(f"https://okpy.org/api/v3/score/", params=params, data=data)
    assert r.status_code == 200, "fail"
    webbrowser.open(f"https://okpy.org/admin/composition/{id}")
    with open(completed, "a") as f:
        f.write(id + "\n")
