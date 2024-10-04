from googleapiclient.discovery import build
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API")
CSE_ID = os.getenv("CSE_ID")

def google_image_search(query, num_results):
    service = build("customsearch", "v1", developerKey=API_KEY)
    
    result = service.cse().list(
        q=query,
        cx=CSE_ID,
        searchType='image',
        num=num_results
    ).execute()
    
    return result.get('items', [])

query = "puppies"
num_images = 3
images = google_image_search(query, num_images)

for i, image in enumerate(images):
    print(f"Image {i+1}: {image['link']}")
