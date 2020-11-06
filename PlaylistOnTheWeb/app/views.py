import base64
import json

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from BaseXClient import BaseXClient
from lxml import etree
import xmltodict
import requests

# Create your views here.

session = BaseXClient.Session('localhost', 1984, 'admin', 'admin')
client_id = '273d90e2d06f4af99f5b53f9e833d2e6'  # Your client id
client_secret = '7a79b1861bee4cbdada76db3784592a1'  # Your secret
redirect_uri = 'http://127.0.0.1:8000/'  # Your redirect uri
scopes = 'user-read-private user-read-email'
auth_url = "https://accounts.spotify.com/api/token"


def get_token():
    auth_response = requests.post(auth_url, {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
    })

    # convert the response to JSON
    auth_response_data = auth_response.json()

    # save the access token
    access_token = auth_response_data['access_token']
    return access_token


def home(request):
    access_token = get_token()
    input = "xquery <root>{ for $a in collection('SpotifyPlaylist')//element/track return <elem> {$a/name} {$a/external_urls/spotify} {$a/album/images/element/url} </elem> } </root>"
    query = session.execute(input)
    # print(query)
    info = dict()
    res = xmltodict.parse(query)
    print(res)
    for c in res["root"]["elem"]:
        print(c)
        info[c["name"]] = dict()
        info[c["name"]]["url"] = c["spotify"]
        info[c["name"]]["imagem"] = c["url"][2]
    print(info.items())
    for nome, url in info.items():
        print(nome)
        print(url)
    tparams = {
        'tracks': info,
        'frase': "Músicas da Playlist Pokémon LoFi:",
    }
    return render(request, "tracks.html", tparams)


def buscar_imagens(url, access_token):
    headers = {
        'Authorization': "Bearer " + access_token
    }
    response = requests.get(url, headers=headers)
    geodata = response.json()
    return geodata["images"][0]["url"]


def artistas(request):
    input = "xquery <root>{ for $a in collection('SpotifyPlaylist')//owner return <elem>{$a}</elem> } </root>"
    query = session.execute(input)
    # print(query)
    info = dict()
    res = xmltodict.parse(query)
    print(res)
    # print(res["root"]["elem"])
    # print(res["root"]["elem"]["owner"]["display_name"])
    # print(res["root"]["elem"]["owner"]["href"])
    access_token = get_token()
    if (len(res["root"]["elem"]) == 1):
        img = buscar_imagens(res["root"]["elem"]["owner"]["href"], access_token)
        info[res["root"]["elem"]["owner"]["display_name"]] = img
    else:
        for c in res["root"]["elem"]:
            print(c)
            img = buscar_imagens(c["owner"]["href"], access_token)
            print(c["display_name"])
            info[c["display_name"]] = img
    print(info.items())

    tparams = {
        'artistas': info,
        'frase': "Artistas:",
    }
    return render(request, "artistas.html", tparams)


def musicas(request):
    return HttpResponse("Musicas!")


def criarPlayList(request):
    return HttpResponse("Cria a tua PlayList!")
