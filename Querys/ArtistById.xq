<root>{  
   for $a in collection('SpotifyPlaylist')//element/track[artists/element/id/text()='5MboRLcEpLbsshOx64OdA6'] 
   return
     <elem>
       {$a/name}
       {$a/external_urls/spotify}
       {($a/album/images/element/url)[last()]}
     </elem>
     
}
</root>