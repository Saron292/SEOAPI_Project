from googleapiclient.discovery import build

API_KEY = 'AIzaSyAp1MmfZ0k3nUq8QHCPxRqjszw6gqm5bXE'

youtube = build('youtube', 'v3', developerKey=API_KEY)

video_id = 'UTcuq1ZiTiI'

request = youtube.videos().list(
    part='snippet,statistics',
    id=video_id
)

response = request.execute()

print(response)