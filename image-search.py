from googleapiclient.discovery import build
import os
from dotenv import load_dotenv
import requests

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

def download_image(url, save_path):
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(save_path, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)

            print(f"Image saved to {save_path}")
        
        else:
            print(f"Failed to retriev image from {url}, Status code: {response.status_code}")
    
    except Exception as e:
        print(f"Error occured while downloading {url}: {e}")

query = "puppies"
num_images = 5
images = google_image_search(query, num_images)

folder = "downloaded_images" # creating a folder to store images
if not os.path.exists(folder):
    os.makedirs(folder)

for i, image in enumerate(images):
    print(f"Image {i+1}: {image['link']}")
    
    file_path = os.path.join(folder, f"image_{i+1}.jpg")
    download_image(image['link'], file_path)