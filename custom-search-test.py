import pprint
from googleapiclient.discovery import build
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API")
CSE_ID = os.getenv("CSE_ID")

def main():
    service = build("customsearch", "v1", developerKey=API_KEY)

    res = (
        service.cse()
        .list(
            q = "lectures",
            cx = CSE_ID,
        )
        .execute()
    )
    pprint.pprint(res)


if __name__ == "__main__":
    main()