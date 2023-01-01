import requests
import base64

# Replace the values below with your own API key and API secret key
api_key = "R47AjI7AIbY4t9xkZLgnxCYfE"
api_secret_key = "86hsbN2nDZTvbdcXNwOaQAL4UN2p3875U5LVDXKJkKU2hXoWlT"

# Encode the API key and API secret key in base64
encoded_api_key_secret = base64.b64encode(f"{api_key}:{api_secret_key}".encode()).decode()

# Obtain a Bearer token
headers = {
    "Authorization": f"Basic {encoded_api_key_secret}",
    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"
}
data = {
    "grant_type": "client_credentials"
}
response = requests.post("https://api.twitter.com/oauth2/token", headers=headers, data=data)

# Extract the Bearer token from the response
bearer_token = response.json()["access_token"]

# Use the Bearer token to authenticate requests to the Twitter API
headers = {
    "Authorization": f"Bearer {bearer_token}"
}

# Retrieve the most recent 100 tweets containing the word "NFT"
response = requests.get("https://api.twitter.com/2/tweets/search/recent", headers=headers, params={
    "query": "\"NFT\"",
    "max_results": 100
})

# Extract the tweets from the response
tweets = response.json()["data"]

# Print the text of each tweet
#for tweet in tweets:
 #   print(tweet["text"])

print(tweets)