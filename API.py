import pandas as pd
import sqlalchemy as db
from googleapiclient.discovery import build

# Your YouTube API key
API_KEY = 'AIzaSyAp1MmfZ0k3nUq8QHCPxRqjszw6gqm5bXE'

# Initialize YouTube API client
youtube = build('youtube', 'v3', developerKey=API_KEY)

# Video ID to fetch
video_id = 'UTcuq1ZiTiI'

# Make request to YouTube Data API
request = youtube.videos().list(
    part='snippet',
    id=video_id
)
response = request.execute()

# Extract the data you want
items = response.get('items', [])
if items:
    video_data = items[0]
    snippet = video_data['snippet']
    
    # Only get the description
    description = snippet.get('description', 'No description found.')
    
    # Print it
    print("\nVideo Description:\n")
    print(description)
    
    # Build minimal DataFrame
    data = {
        'video_id': [video_id],
        'description': [description]
    }
    df = pd.DataFrame(data)
    
    # Save to SQLite
    engine = db.create_engine('sqlite:///data_base_name.db')
    df.to_sql('table_name', con=engine, if_exists='replace', index=False)
    print("\nSaved to database: data_base_name.db (table: table_name)")
    
    # Read back and show
    with engine.connect() as connection:
        query_result = connection.execute(db.text("SELECT * FROM table_name;")).fetchall()
        print("\nData read back from database:\n")
        print(pd.DataFrame(query_result))
else:
    print("No video found for given ID.")

# print(response)