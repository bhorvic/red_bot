import requests
from access_token import access_token

def send_private_message(access_token, subject, body, recipient):
    url = "https://oauth.reddit.com/api/compose"
    headers = {
        "Authorization": f"bearer {access_token}",
        "User-Agent": "YourBot/1.0"  # Replace "YourBot/1.0" with your bot's user agent
    }
    data = {
        "api_type": "json",
        "subject": subject,
        "text": body,
        "to": recipient
    }
    response = requests.post(url, headers=headers, data=data)
    response_json = response.json()
    
    if 'errors' in response_json['json'] and response_json['json']['errors'][0][0] == 'RESTRICTED_TO_PM':
        print("Cannot send message, user doesn't accept direct messages.")
    else:
        print(response_json)

    return response_json

# Replace these variables with your actual values
subject = "Test Message"
body = "This is a test message sent via Reddit API."
recipient = "bhorvic"

response = send_private_message(access_token, subject, body, recipient)
print(response)
