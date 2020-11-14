import base64
import json

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from BaseXClient import BaseXClient
from lxml import etree
import xmltodict
import requests
import random
from lxml import etree
import datetime

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

def criarxml(Id, name, numeroMusicas, musicasInfo): # musicas é dict
    playlistDemo = etree.Element("playlistDemo", id=Id)
    nome = etree.SubElement(playlistDemo,"nome")
    nome.text = name
    id = etree.SubElement(playlistDemo, "id")
    id.text = Id
    numeroDeMusicas = etree.SubElement(playlistDemo, "numeroDeMusicas")
    numeroDeMusicas.text = numeroMusicas
    dataCriacao = etree.SubElement(playlistDemo, "dataCriacao")
    dataCriacao.text = str(datetime.date.today())
    musicas = etree.SubElement(playlistDemo,"musicas")
    for n, dados in musicasInfo.items():
        musica = etree.SubElement(musicas,"musica")
        nome = etree.SubElement(musica,"nome")
        nome.text = n
        id = etree.SubElement(musica, "id")
        id.text = dados["id"]
        externalUrl = etree.SubElement(musica,"externalUrl")
        externalUrl.text = dados["externalUrl"]
        img = etree.SubElement(musica,"img")
        img.text = dados["img"]
        artistas = etree.SubElement(musica,"artistas")
        for a, i in dados["artistas"].items():
            artista = etree.SubElement(artistas,"artista")
            nome = etree.SubElement(artista,"nome")
            nome.text = a
            id = etree.SubElement(artista,"id")
            id.text = i

    print(etree.tostring(playlistDemo))
    xsd_root = etree.parse("files/example.xsd")
    schema = etree.XMLSchema(xsd_root)
    print(schema.validate(playlistDemo))
    input = "xquery let $bs := collection('SpotifyPlaylist') for $b in $bs return insert node " + etree.tostring(playlistDemo).decode("utf-8") + " after $b//playlist"
    print(input)
    session.execute(input)



def home(request):
    input = "xquery import module namespace funcsPlaylist = 'com.funcsPlaylist.my.index'; funcsPlaylist:home()"
    query = session.execute(input)
    # print(query)
    info = dict()
    res = xmltodict.parse(query)
    # print(res)
    count = 0
    for i in range(4):
        # print(c)
        c = random.choice(res["root"]["elem"])
        print(c)
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

    tparams = {
        'tracks': info,
        'frase': "Home:",
    }
    return render(request, "home.html", tparams)


def musicas(request):
    access_token = get_token()
    input = "xquery import module namespace funcsPlaylist = 'com.funcsPlaylist.my.index'; funcsPlaylist:musicas()"
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
    input = "xquery import module namespace funcsPlaylist = 'com.funcsPlaylist.my.index'; funcsPlaylist:artist-tracks('{}')".format(id)
    input_name = "xquery import module namespace funcsPlaylist = 'com.funcsPlaylist.my.index'; funcsPlaylist:artist-name('{}')".format(id)
    query = session.execute(input)
    # print(query)
    art_name = session.execute(input_name)
    # info = dict()
    # res = xmltodict.parse(query)
    res_name = xmltodict.parse(art_name)
    # if isinstance(res["root"]["elem"], list):
    #     for a in res["root"]["elem"]:
    #         info[a["name"]] = dict()
    #         info[a["name"]]["url"] = a["spotify"]
    #         info[a["name"]]["imagem"] = a["url"]
    #         info[a["name"]]["embed"] = a["spotify"][:25] + 'embed/' + a["spotify"][25:]
    # else:
    #     a = res["root"]["elem"]
    #     info[a["name"]] = dict()
    #     info[a["name"]]["url"] = a["spotify"]
    #     info[a["name"]]["imagem"] = a["url"]
    #     info[a["name"]]["embed"] = a["spotify"][:25] + 'embed/' + a["spotify"][25:]

    xml = etree.fromstring(query)
    xslt_file = etree.parse("files/artist_tracks.xsl")
    transform = etree.XSLT(xslt_file)
    html = transform(xml)

    tparams = {
        'artistas': False,
        'tracks': html,
        'frase': "Músicas do Artistas: " + res_name["root"]["name"]
    }
    return render(request, "artist_tracks.html", tparams)


def artistas(request):
    input = "xquery import module namespace funcsPlaylist = 'com.funcsPlaylist.my.index'; funcsPlaylist:buscar-artistas() "
    query = session.execute(input)
    # print(query)
    # info = dict()

    # res = xmltodict.parse(query)
    # print(res)
    # print(res["root"]["elem"])
    # print(res["root"]["elem"]["owner"]["display_name"])
    # print(res["root"]["elem"]["owner"]["href"])
    # if len(res["root"]["artista"]) == 1:
    #     info[res["root"]["artista"]["name"]] = dict()
    #     info[res["root"]["artista"]["name"]]["id"] = res["root"]["artista"]["id"]
    #     info[res["root"]["artista"]["name"]]["imagem"] = res["root"]["artista"]["imagem"]
    # else:
    #     for c in res["root"]["artista"]:
    #         info[c["name"]] = dict()
    #         info[c["name"]]["id"] = c["id"]
    #         info[c["name"]]["imagem"] = c["imagem"]
    # print(info.items())

    xml = etree.fromstring(query)
    xslt_file = etree.parse("files/artistas.xsl")
    transform = etree.XSLT(xslt_file)
    html = transform(xml)
    # print(html)

    tparams = {
        'artistas': html,
        'frase': "Artistas:",
    }
    return render(request, "artistas.html", tparams)


def albums(request):
    input = "xquery import module namespace funcsPlaylist = 'com.funcsPlaylist.my.index'; funcsPlaylist:albums() "
    query = session.execute(input)

    xml = etree.fromstring(query)
    xslt_file = etree.parse("files/albums.xsl")
    transform = etree.XSLT(xslt_file)
    html = transform(xml)

    tparams = {
        'albums': html,
        'frase': "Albums:",
    }
    return render(request, "albums.html", tparams)

#def criarPlayList(request):
#    input = "xquery import module namespace funcsPlaylist = 'com.funcsPlaylist.my.index'; funcsPlaylist:buscar-artistas()"
#    query = session.execute(input)
#   access_token = get_token()
#    if len(res["root"]["artista"]) == 1:
#        img = buscar_imagens(res["root"]["artista"]["href"], access_token)
#        insert = "xquery import module namespace funcsPlaylist = 'com.funcsPlaylist.my.index'; funcsPlaylist:insert-imagem-artista('{}','{}')".format(res["root"]["artista"]["id"],img)
#        session.execute(insert)
#    else:
#        for c in res["root"]["artista"]:
#            img = buscar_imagens(c["href"], access_token)
#            insert = "xquery import module namespace funcsPlaylist = 'com.funcsPlaylist.my.index'; funcsPlaylist:insert-imagem-artista('{}','{}')".format(
#                c["id"], img)
#            session.execute(insert)
#
#    return HttpResponse("Cria a tua PlayList!")

def criarPlayList(request):

    nomeMusicas = []

    if 'nameMusica' in request.POST:
        print(request.POST)
        nomes = request.POST.getlist('nameMusica')
        print(nomes)
        musicas = dict()
        for nMusicas in nomes:
            print(nMusicas)
            input = "xquery import module namespace funcsPlaylist = 'com.funcsPlaylist.my.index'; funcsPlaylist:info-musica('{}')".format(nMusicas)
            query = session.execute(input)
            res = xmltodict.parse(query)
            print(res["root"]["elem"])
            musica = res["root"]["elem"]
            musicas[musica["name"]] = dict()
            musicas[musica["name"]]["id"] = musica["id"]
            musicas[musica["name"]]["externalUrl"] = musica["spotify"]
            musicas[musica["name"]]["img"] = musica["url"]
            musicas[musica["name"]]["artistas"] = dict()
            if isinstance(musica["artista"], list):
                for art in musica["artista"]:
                    musicas[musica["name"]]["artistas"][art["name"]] = art["id"]
            else:
                musicas[musica["name"]]["artistas"][art["name"]] = art["id"]

        criarxml("1","teste","2",musicas)




    access_token = get_token()
    input = "xquery import module namespace funcsPlaylist = 'com.funcsPlaylist.my.index'; funcsPlaylist:musicas()"
    query = session.execute(input)
    # print(query)
    info = dict()
    res = xmltodict.parse(query)
    # print(res)
    for c in res["root"]["elem"]:
        # print(c)
        info[c["name"]] = dict()
        info[c["name"]]["url"] = c["spotify"]
        info[c["name"]]["id"] = c["id"]
        info[c["name"]]["imagem"] = c["url"][2]
        # info[c["name"]]["embed"] = c["spotify"][:25] + 'embed/' + c["spotify"][25:]
        info[c["name"]]["artistas"] = dict()
        if isinstance(c["artista"], list):
            for art in c["artista"]:
                info[c["name"]]["artistas"][art["name"]] = art["id"]
        else:
            info[c["name"]]["artistas"][c["artista"]["name"]] = c["artista"]["id"]

    #print(info.items())
    # for nome, url, embed in info.items():
    #     print(nome)
    #     print(url)
    #     print(embed)
    tparams = {
        'artistas': True,
        'tracks': info,
        'frase': "Músicas da Playlist Pokémon LoFi:",
    }
    return render(request, "criarPlayList.html", tparams)

def myPlayList(request):
    input = "xquery <root>{for $a in collection('SpotifyPlaylist')//playlistDemo return $a }</root>"
    query = session.execute(input)

    xml = etree.fromstring(query)
    xslt_file = etree.parse("files/myPlayList.xsl")
    transform = etree.XSLT(xslt_file)
    html = transform(xml)

    tparams = {
        'playlist': html,
        'frase': "Playlist:",
    }
    return render(request, "myPlayList.html", tparams)

def playlist(request):
    #if request.method == "POST":
        #form = MyForm(request.POST)
        #e = request.POST.getlist("choice_field")

    c = {'form': 'ola'}

    print('ola')
    print(request.POST)
    return render(request,"playlist.html", c)
