from fastapi import FastAPI, APIRouter, Body, Path, HTTPException, status, HTTPException
from typing import Optional, List
import requests
import json

from apps.trends.schemas import QueryBase, QueryResponse

router = APIRouter()

@router.get(path="/", response_model=List[QueryResponse], status_code=status.HTTP_200_OK, summary="Get top 10 queries")
async def show_trends():

    query = await QueryBase.find_all().sort([( '$natural', -1 )]).limit(10).to_list()

    if not query:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Queries are empty"
        )
    return query



# Add query
@router.post(path="/", response_model=QueryResponse, status_code=status.HTTP_201_CREATED, summary="Create a query")
async def post_query(query: QueryBase = Body(...,  title="Post new query",
                                                              description="Post new query",
                                                              )):
    await query.create()
    if not query:
        raise HTTPException(status_code=404,
                            detail="Error creating query")
    return query


