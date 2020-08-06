import requests

url = "https://matchilling-tronald-dump-v1.p.rapidapi.com/search/quote"

querystring = {"query":"{query}?page=The page number","size":"25"}

headers = {
    'x-rapidapi-host': "matchilling-tronald-dump-v1.p.rapidapi.com",
    'x-rapidapi-key': "SIGN-UP-FOR-KEY",
    'accept': "application/hal+json"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)