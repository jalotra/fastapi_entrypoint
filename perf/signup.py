from locust import FastHttpUser, task
import requests
import uuid
import json
import random
import os
random.seed(40)

HOST = os.environ.get("HOST") if os.environ.get("HOST") is not None else "localhost"
PORT = os.environ.get("PORT") if os.environ.get("PORT") is not None else "8890"
USERS = []
PASSWORDS = []

# Generates a new user <username, password>
def user_signup():
  username = uuid.uuid4().hex
  password = uuid.uuid4().hex

  # Retries 3 times
  for i in range(3):
    url = f"http://{HOST}:{PORT}/signup"

    payload = json.dumps({
      "username": f"{username}",
      "password": f"{password}"
    })
    headers = {
      'accept': 'application/json',
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    if response.status_code == 200:
      global USERS, PASSWORDS
      USERS.append(username)
      PASSWORDS.append(password)
      break


def login_perf_test(client, usernames : list[str], passwords : list[str]):
  idx = random.randint(0, len(usernames) - 1)
  url = f"http://{HOST}:{PORT}/login"
  payload = f'grant_type=&username={usernames[idx]}&password={passwords[idx]}&scope=&client_id=&client_secret='
  headers = {
    'accept': 'application/json',
    'Content-Type': 'application/x-www-form-urlencoded'
  }
  response = client.post(url, headers=headers, data=payload)

  return response.status_code == 200

class LoginTest(FastHttpUser):
  # generate 1000 fake usernames and passwords
  for i in range(10):
    user_signup()
  print(USERS, PASSWORDS)

  @task
  def send_login_req(self):
    login_perf_test(self.client, usernames=USERS, passwords=PASSWORDS)

