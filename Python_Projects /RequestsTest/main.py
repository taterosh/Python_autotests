import requests
import json

token = 'f0f2f3dea4b27945d90ae8c238d16261'


response = requests.post('https://pokemonbattle.me:5000/pokemons', json = {
    'name': 'Мяут',
    'photo': 'https://www.kindpng.com/picc/m/165-1653905_meowth-pokemon-hd-png-download.png'
}, headers = {'Content-Type': 'application/json', 'trainer_token' : token })

print(response.text)

pokemon_id = response.json()['id']

response_change = requests.put('https://pokemonbattle.me:5000/pokemons', json = {
    'pokemon_id': pokemon_id,
    'name': 'Meowth',
    'photo': 'https://avatanplus.com/files/resources/original/57ad58e44eae71567d233be2.png'
}, headers = {'Content-Type': 'application/json', 'trainer_token' : token })

print(response_change.text)


response_catсh = requests.post('https://pokemonbattle.me:5000/trainers/add_pokeball', json = {
    'pokemon_id': 3133
}, headers = {'Content-Type': 'application/json', 'trainer_token' : token })

print(response_catсh.text)