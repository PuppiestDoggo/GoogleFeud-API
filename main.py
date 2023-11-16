from fastapi import FastAPI
import requests, json
app = FastAPI()

headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 "
    "Safari/537.36 Edge/18.19582"
}


@app.get("/query/{query}")
async def query(query: str):
    response = requests.get(f'https://google.com/complete/search?client=chrome&q={query}',
                            headers=headers)
    results = []
    for result in json.loads(response.text)[1]:
        results.append(result)

    return {"Reponses": f"{results}"}
