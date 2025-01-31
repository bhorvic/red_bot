import requests
from red_bot_config import client_id, client_secret, username, password

token_file = "access_token.txt"

def get_access_token(client_id, client_secret, username, password):
    auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
    data = {
        "grant_type": "password",
        "username": username,
        "password": password
    }
    headers = {"User-Agent": "MyBot/1.0"}
    response = requests.post("https://www.reddit.com/api/v1/access_token", auth=auth, data=data, headers=headers)
    return response.json()

token_response = get_access_token(client_id, client_secret, username, password)
access_token = token_response["access_token"]

# Save the access token to a local text file
with open(token_file, "w") as f:
    f.write(access_token)

print("OAuth Token saved to", token_file)
