from fastapi import APIRouter, Body, FastAPI, status, Response
from typing import Optional, List
import requests
import json

from apps.search.schemas import UserBase

router = APIRouter()

@router.get("/{username}", status_code=status.HTTP_200_OK, summary="Show all users",)
async def read_user(username: str):
    resultl = search_user_by_id(username)
    return resultl

def search_user_by_id(username: str):
    url = "https://torre.ai/api/entities/_searchStream"
    payload = json.dumps({
    "query": username,
    "identityType": "person",
    "meta": False,
    "limit": 10,
    "torreGgId": "1125867",
    "excludeContacts": True,
    "excludedPeople": []
    })
    headers = {
    'Content-Type': 'application/json',
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    result = xndjson_to_json(response.text)
      
    return result


def xndjson_to_json(xndjson):
    result = []

    for ndjson_line in xndjson.splitlines():
        if not ndjson_line.strip():
            continue  # ignore empty lines
        json_line = json.loads(ndjson_line)
        result.append(json_line)
    
    return result