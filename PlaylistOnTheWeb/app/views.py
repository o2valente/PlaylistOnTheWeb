import base64
import json

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from BaseXClient import BaseXClient
from lxml import etree
import xmltodict
import requests
import random

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
    input = "xquery <root>{ for $a in collection('SpotifyPlaylist')//element/track return <elem> {$a/name} {" \
            "$a/external_urls/spotify} {$a/album/images/element/url} { for $b in $a/artists/element return <artista> " \
            "{$b/name} {$b/id} </artista> } </elem> } </root> "
    query = session.execute(input)
    # print(query)
    info = dict()
    res = xmltodict.parse(query)
    # print(res)
    count = 0
    for c in res["root"]["elem"]:
        # print(c)
        c = random.choice(res["root"]["elem"])
        print(c)
        if count < 4:
            info[c["name"]] = dict()
            info[c["name"]]["url"] = c["spotify"]
            info[c["name"]]["imagem"] = c["url"][2]
            # info[c["name"]]["embed"] = c["spotify"][:25] + 'embed/' + c["spotify"][25:]
            info[c["name"]]["artistas"] = dict()
            if isinstance(c["artista"], list):
                for art in c["artista"]:
                    info[c["name"]]["artistas"][art["name"]] = art["id"]
            else:
                info[c["name"]]["artistas"][c["artista"]["name"]] = c["artista"]["id"]
        count += 1

    tparams = {
        'tracks': info,
        'frase': "Home:",
    }
    return render(request, "home.html", tparams)


def musicas(request):
    access_token = get_token()
    input = "xquery <root>{ for $a in collection('SpotifyPlaylist')//element/track return <elem> {$a/name} {" \
            "$a/external_urls/spotify} {$a/album/images/element/url} { for $b in $a/artists/element return <artista> " \
            "{$b/name} {$b/id} </artista> } </elem> } </root> "
    query = session.execute(input)
    # print(query)
    info = dict()
    res = xmltodict.parse(query)
    # print(res)
    for c in res["root"]["elem"]:
        # print(c)
        info[c["name"]] = dict()
        info[c["name"]]["url"] = c["spotify"]
        info[c["name"]]["imagem"] = c["url"][2]
        # info[c["name"]]["embed"] = c["spotify"][:25] + 'embed/' + c["spotify"][25:]
        info[c["name"]]["artistas"] = dict()
        if isinstance(c["artista"], list):
            for art in c["artista"]:
                info[c["name"]]["artistas"][art["name"]] = art["id"]
        else:
            info[c["name"]]["artistas"][c["artista"]["name"]] = c["artista"]["id"]

    print(info.items())
    # for nome, url, embed in info.items():
    #     print(nome)
    #     print(url)
    #     print(embed)
    tparams = {
        'artistas': True,
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


def artist_tracks(request):
    id = str(request.GET.get('id'))
    input = "xquery <root>{ for $a in collection('SpotifyPlaylist')//element/track[artists/element/id/text()='" + id + \
            "'] return <elem> {$a/name} {$a/external_urls/spotify} {($a/album/images/element/url)[last()]} </elem> } " \
            "</root> "
    input_name = "xquery <root>{ let $q := (collection('SpotifyPlaylist')//track/artists/element[id/text() ='" + id + \
                 "'])[last()] return $q/name }</root> "
    query = session.execute(input)
    art_name = session.execute(input_name)
    info = dict()
    res = xmltodict.parse(query)
    res_name = xmltodict.parse(art_name)
    if isinstance(res["root"]["elem"], list):
        for a in res["root"]["elem"]:
            info[a["name"]] = dict()
            info[a["name"]]["url"] = a["spotify"]
            info[a["name"]]["imagem"] = a["url"]
            info[a["name"]]["embed"] = a["spotify"][:25] + 'embed/' + a["spotify"][25:]
    else:
        a = res["root"]["elem"]
        info[a["name"]] = dict()
        info[a["name"]]["url"] = a["spotify"]
        info[a["name"]]["imagem"] = a["url"]
        info[a["name"]]["embed"] = a["spotify"][:25] + 'embed/' + a["spotify"][25:]
    tparams = {
        'artistas': False,
        'tracks': info,
        'frase': "Músicas do Artistas: " + res_name["root"]["name"]
    }
    return render(request, "artist_tracks.html", tparams)


def artistas(request):
    input = "xquery <root>{ for $a in distinct-values(collection('SpotifyPlaylist')//track/artists/element/name) let " \
            "$b := (collection('SpotifyPlaylist')//track/artists/element[name = $a])[1] return<artista>{$b/href} {" \
            "$b/id} {$b/name}</artista>}</root> "
    query = session.execute(input)
    # print(query)
    info = dict()

    res = xmltodict.parse(query)
    print(res)
    # print(res["root"]["elem"])
    # print(res["root"]["elem"]["owner"]["display_name"])
    # print(res["root"]["elem"]["owner"]["href"])
    access_token = get_token()
    if len(res["root"]["artista"]) == 1:
        img = buscar_imagens(res["root"]["artista"]["href"], access_token)
        info[res["root"]["artista"]["name"]] = dict()
        info[res["root"]["artista"]["name"]]["id"] = res["root"]["artista"]["id"]
        info[res["root"]["artista"]["name"]]["imagem"] = img
    else:
        for c in res["root"]["artista"]:
            img = buscar_imagens(c["href"], access_token)
            info[c["name"]] = dict()
            info[c["name"]]["id"] = c["id"]
            info[c["name"]]["imagem"] = img
    print(info.items())

    tparams = {
        'artistas': info,
        'frase': "Artistas:",
    }
    return render(request, "artistas.html", tparams)


def criarPlayList(request):
    return HttpResponse("Cria a tua PlayList!")
