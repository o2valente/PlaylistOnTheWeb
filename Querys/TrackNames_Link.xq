<root>{ 
  for $a in collection('SpotifyPlaylist')//element/track
  return 
    <elem> 
      {$a/name} 
       {$a/external_urls/spotify} 
       </elem> 
} 
</root>