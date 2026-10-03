from http.client import responses

from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup
import time
app = FastAPI()
# Cache storage
cache_data = []
last_fetch = 0


@app.get("/news")
def get_news():
    global cache_data , last_fetch

    start = time.time()

    if time.time() - last_fetch > 60:
        print("Fetching Fresh Data")

        url = "https://news.ycombinator.com/"

        response = requests.get(url)

        soup = BeautifulSoup(response.text, "html.parser")

        cache_data= [
            item.text for item in soup.find_all("tr", class_="athing submission" )

        ]


        last_fetch = time.time()

    else:

        print("using caching data")

    end = time.time()

    time_taken = round (end - start )

    print ("Time taken : ", time_taken)

    return {
        "time_taken": time_taken,
        "data": cache_data[:5]

    }






