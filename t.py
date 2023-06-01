import requests

url = "https://t.me/my_channel"
response = requests.get(url).content

# print(response)
# u = response[
#     response.index('src="https://cdn4.telegram-cdn.org/file') : response.index("></a>")
# ]
# print(u)

print(response.index("tgme_page_photo_image"))
