from fastapi import FastAPI, APIRouter, Body, Path, HTTPException, status, HTTPException
from typing import Optional, List
import requests
import json

from apps.trends.schemas import UserBase, UserBaseResponse

router = APIRouter()

@router.get("/", status_code=status.HTTP_200_OK, summary="Show most wanted",)
async def show_most_wanted():
    return {}

# Create training sesion
@router.post(path="/", response_model=UserBaseResponse, status_code=status.HTTP_201_CREATED, summary="Create a query")
async def post_query(query: UserBase = Body(...,  title="Post new query",
                                                              description="Post new query",
                                                              )):
  
    await query.create()
    if not query:
        raise HTTPException(status_code=404)
    return query

