import json
import uuid
import boto3


def lambda_handler(event, context):
    # TODO implement
    s3 = boto3.client('s3')
    
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
            
        songs.append(', '.join(song))
    
    s3.put_object(Body='\n'.join(songs), Bucket='zali-gold-song-bucket', Key=str(uuid.uuid4()) + '.txt')
    
    print(songs)