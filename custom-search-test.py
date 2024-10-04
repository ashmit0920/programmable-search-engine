import pprint
from googleapiclient.discovery import build

def main():
    service = build("customsearch", "v1", developerKey="AIzaSyAhyV5S_wKK9ZkV12nV9ETyCiw1dNSdjJ4")

    res = (
        service.cse()
        .list(
            q="lectures",
            cx="017576662512468239146:omuauf_lfve",
        )
        .execute()
    )
    pprint.pprint(res)


if __name__ == "__main__":
    main()