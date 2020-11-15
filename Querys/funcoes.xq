module namespace funcsPlaylist = "com.funcsPlaylist.my.index";

declare updating function funcsPlaylist:insert-imagem-artista($aid, $alink){
  for $a in collection('SpotifyPlaylist')//artists/element where $a/id = $aid
   return insert node <imagem>{$alink}</imagem> after $a/uri
};

declare updating function funcsPlaylist:delete-playlist($id){
  let $n := (collection('SpotifyPlaylist')//newPlaylist/playlistDemo[id/text()=$id]) 
  return delete node $n 
};

declare function funcsPlaylist:buscar-artistas() as element()*{
  <root>{ 
  for $a in distinct-values(collection('SpotifyPlaylist')//track/artists/element/name) 
        let $b := (collection("SpotifyPlaylist")//track/artists/element[name = $a])[1] 
          return
            <artista>{$b/href} {$b/id} {$b/name} {$b/imagem}</artista>
          
  }
  </root>
};

declare function funcsPlaylist:artist-tracks($aid){
  <root>{ for $a in collection('SpotifyPlaylist')//element/track[artists/element/id/text()=$aid] 
  return <elem> {$a/name} {$a/external_urls/spotify} {($a/album/images/element/url)[last()]} </elem> 
}</root>
};

declare function funcsPlaylist:artist-name($aid){
 <root>{ 
  let $q := (collection('SpotifyPlaylist')//track/artists/element[id/text()=$aid])[last()] return $q/name 
 }</root>
};

declare function funcsPlaylist:home(){
  <root>{ 
    for $a in collection('SpotifyPlaylist')//element/track 
    return <elem>
         {$a/name} {$a/external_urls/spotify} {$a/album/images/element/url} { 
         for $b in $a/artists/element 
         return <artista>
          {$b/name} {$b/id} </artista> } </elem> } </root>
};

declare function funcsPlaylist:musicas(){
  <root>{ 
    for $a in collection('SpotifyPlaylist')//element/track 
    return <elem> 
      {$a/name} 
      {$a/external_urls/spotify}
      {$a/id}
      {$a/album/images/element/url} { 
      for $b in $a/artists/element
       return <artista> {$b/name} {$b/id} </artista> } </elem> } </root>
};

declare function funcsPlaylist:info-musica($id){
  <root>{
      for $a in collection('SpotifyPlaylist')//element/track[id/text()=$id]
      return <elem>
          {$a/name}
          {$a/id}
          {$a/external_urls/spotify}
          {($a/album/images/element/url)[last()]} {
          for $b in $a/artists/element
           return <artista> {$b/name} {$b/id} </artista> }
          </elem>
  }</root>
};

declare function funcsPlaylist:albums(){
   <root>{ 
    for $a in distinct-values(collection('SpotifyPlaylist')//element/track/album/name)
      let $b := (collection("SpotifyPlaylist")//track/album[name = $a])[1] 
        return <album> 
          {$b/name} 
          {$b/release_date}
          {$b/total_tracks}
          {($b/images/element/url)[last()]}
          {$b/external_urls/spotify}
          {$b/id}
          {$b/album/images/element/url} { 
          for $c in $b/artists/element
           return <artista> {$c/name} {$c/id} </artista> } 
        </album> 
  }</root>
};

declare function funcsPlaylist:last-playlistID(){
   let $id := (collection('SpotifyPlaylist')//newPlaylist/playlistDemo/id)
   return $id[last()]
};





