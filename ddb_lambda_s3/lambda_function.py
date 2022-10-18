import json

def lambda_handler(event, context):
    # TODO implement
    
    print(event)
    
    songs = []
    records = event['Records']
    
    for record in records:
        data = record['dynamodb']['NewImage']
        
        song = []
        for k, v in data.items():
            try:
                song.append(v["S"])
            except:
                pass
            
        songs.append(' '.join(song))
    
    print(songs)