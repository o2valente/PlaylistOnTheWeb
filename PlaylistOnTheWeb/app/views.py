from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from BaseXClient import BaseXClient
from lxml import etree
import xmltodict
import requests
# Create your views here.

session = BaseXClient.Session('localhost', 1984, 'admin', 'admin')

def home(request):
    input = "xquery <root>{ for $a in collection('SpotifyPlaylist')//element/track return <elem> {$a/name} {$a/external_urls/spotify} {$a/album/images/element/url} </elem> } </root>"
    query = session.execute(input)
    #print(query)
    info = dict()
    res = xmltodict.parse(query)
    print(res)
    for c in res["root"]["elem"]:
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

def artistas(request):
    input = "xquery <root>{ for $a in collection('SpotifyPlaylist')//owner return <elem>{$a}</elem> } </root>"
    query = session.execute(input)
    # print(query)
    info = dict()
    res = xmltodict.parse(query)
    print(res)
    print(res["root"]["elem"])
    print(res["root"]["elem"]["owner"]["display_name"])
    #for c in res["root"]["elem"]["owner"]:
        #info[c["name"]] = dict()
        #info[c["name"]]["display_name"] = c["display_name"]
        #info[c["display_name"]]["owner"] = c[0]
        #info[c["name"]]["imagem"] = c["url"][2]
    print(info.items())
    info["display_name"] = res["root"]["elem"]["owner"]["display_name"]

    url = 'https://api.spotify.com/v1/users/' + res["root"]["elem"]["owner"]["display_name"]
    headers = {'Authorization': 'Bearer BQBctdWWh7HraUnNIEMAyZ5B-WHJrTdfs2kLFeCG96tl6lmiC1hItCd5MSfIJx8jMawne_rnsi0HUzFD3mUSbAfId8RIIFHbvmYOOexVeUCYdHJ1cMCtZk_4pPb2Do45tMnoiQL0r4uqtqRz5uaGGk7kihlWcXr6CDOh23mufHDz_FZM'}
    response = requests.get(url, headers=headers)
    geodata = response.json()
    #img = geodata["images"][0]["url"]

    tparams = {
        'artistas': info,
        #'img': img,
        'frase': "Artistas:",
    }
    return render(request, "artistas.html", tparams)

def musicas(request):
    return HttpResponse("Musicas!")

def criarPlayList(request):
    return HttpResponse("Cria a tua PlayList!")