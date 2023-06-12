import requests
import json

BASE_URL = "http://127.0.0.1:8000/api/users"

def create_user(username, name, user_id):
    url = f"{BASE_URL}/bot-users/"
    response = requests.get(url=url).text
    data = json.loads(response)
    user_exist = False
    for i in data:
        if i["user_id"] == str(user_id):
            user_exist = True
            break
    if user_exist == False:
        requests.post(url=url, data={"username":username, "name":name, "user_id":user_id})
        return "User created"

    else:
        return "User exists"




def create_feedback(name, user_id, body):
    url = f"{BASE_URL}/feedback/"
    if body and user_id and name:
        post = requests.post(url=url, data={
            "name":name,
            "user_id":user_id,
            "body":body
        })
        return "Sent to admin Thanks for your feedback"
    else:
        return "The action is not over"
