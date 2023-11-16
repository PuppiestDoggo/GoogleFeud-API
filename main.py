import json
import random

import requests
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
queries = ["Are dogs ", "Are puppies ", "Are humans ", "Are cats ", "Do humans ", "Do robots ", "Is it bad to ",
           "Is it good to "],
headers = {
    "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 "
        "Safari/537.36 Edge/18.19582"
}


class AnswersModel(BaseModel):
    answers: list


@app.get("/getquery/")
async def get_query():
    n = len(queries[0])
    return queries[0][random.randint(0,n)]


@app.get("/query/{query}")
async def query(query: str):
    response = requests.get(f'https://google.com/complete/search?client=chrome&q={query}',
                            headers=headers)
    results = []
    for result in json.loads(response.text)[1]:
        results.append(result)
    return AnswersModel(answers=results)
