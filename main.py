import json
import requests

# Client voor het opvragen van Oauth Token met credentials
# By Security Advanced Team 2
# Installatiedetails --> readme.md

# Todo token_url: in de api kijken wat dit precies doet --> genereren van token? via oauth????
token_url = "https://ventielshop.dubbadub.be:8081/connect/token"
# api_url: enkel zichtbaar met een token
api_url = "https://ventielshop.dubbadub.be/fiets"

# Voorgedefinieerde credentials
client_id = 'pxl-secadv'
client_secret = 'maarten_lust_geen_spruitjes'

# data: Hiermee geef je aan dat je een Token wilt op basis van client credentials
data = {'grant_type': 'client_credentials'}

# stap 1 - single call met client credentials als basic Oauth header, deze geeft de token terug

# Todo access_token_response: waar gaat deze data heen in de api??
access_token_response = requests.post(token_url, data=data, verify=False, allow_redirects=False, auth=(client_id, client_secret))
print("Access Token Response:")
print(access_token_response.headers)

print("Access Token")
print(access_token_response.text)

# Todo tokens: json.loads??
tokens = json.loads(access_token_response.text)

print("access token: " + tokens['access_token'])

# stap 2 - Met de verkregen access_token kunnen we zoveel calls maken als we willen

# Todo: zoveels calls als we willen? waarom is dit nodig?
api_call_headers = {'Authorization': 'Bearer ' + tokens['access_token']}
api_call_response = requests.get(api_url, headers=api_call_headers, verify=False)

print(api_call_response.text)

# Todo: Waar zitten de vulnerabilities?