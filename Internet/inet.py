import requests

api_key = "8JP9wmIwKcAr8WazfOOHKjyu7Sdisna6"
base_url = "https://api.giphy.com/v1/gifs/"
end_point = "trending"

params = {'api_key' : api_key,
          'limit' : 5}

response = requests.get(base_url + end_point, params = params)

if not response:
    raise Exception(f"Error {response.status_code}")

for gif in response.json()['data']:
    print(f"Title = {gif['title']}, URL = {gif['images']['original']['mp4']}")

    title = gif['title']
    response_img = requests.get(gif['images']['original']['mp4'])

    if response_img:
        with open(f"{title}.mp4", "wb") as f:
            f.write(response_img.content)




