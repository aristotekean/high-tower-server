from fastapi import FastAPI, APIRouter, Body, Path, HTTPException, status, HTTPException
from typing import Optional, List
import requests
import json

from apps.trends.schemas import QueryBase, QueryResponse

router = APIRouter()

@router.get("/", status_code=status.HTTP_200_OK, summary="Show most wanted",)
async def show_most_wanted():
    return {}

# Add query
@router.post(path="/", response_model=QueryResponse, status_code=status.HTTP_201_CREATED, summary="Create a query")
async def post_query(query: QueryBase = Body(...,  title="Post new query",
                                                              description="Post new query",
                                                              )):
    print(query)
    await query.create()
    if not query:
        raise HTTPException(status_code=404)
    return query

