<root>{
  let $q := (collection("SpotifyPlaylist")//track/artists/element[id/text() ="5MboRLcEpLbsshOx64OdA6"])[1]
  return
    $q/name
}</root>