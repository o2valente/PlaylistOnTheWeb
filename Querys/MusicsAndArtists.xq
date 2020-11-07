<root>{
for $a in collection('SpotifyPlaylist')//element/track
return
     <elem>
          {$a/name}
          {$a/external_urls/spotify}
          {$a/album/images/element/url}
          <artistas>{
            for $b in $a/artists/element
            return
              <artista>
                {$b/name}
                {$b/id}
              </artista>
          }
          </artistas>
      </elem> 
} 
</root>