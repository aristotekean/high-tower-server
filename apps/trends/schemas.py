from beanie import Document, PydanticObjectId
from typing import Optional
from pydantic import (Field)


class QueryBase(Document):
    query: str = Field(...)
    
    class Settings:
        name = "trends"
    
    class Config:
        schema_extra = {
        "query": "string"
        }

class QueryResponse(QueryBase):
    _id: PydanticObjectId


class UserBase(Document):
    ardaId: Optional[int] = Field()
    ggId: Optional[str] = Field()
    name: Optional[str] = Field()
    comparableName: Optional[str] = Field()
    username: Optional[str] = Field()
    professionalHeadline: Optional[str] = Field()
    imageUrl: Optional[str] = Field()
    completion: Optional[float] = Field()
    grammar: Optional[float] = Field()
    weight: Optional[bool] = Field()
    connections: Optional[list] = Field()
    totalStrength: Optional[bool] = Field()
    pageRank:  Optional[float] = Field()
    organizationId: Optional[int]  = Field()
    organizationNumericId: Optional[int]  = Field()
    status: Optional[int]  = Field()
    creators: Optional[list]  = Field()
    relationDegree: Optional[int]  = Field()
    contact: Optional[bool]  = Field()

    class Settings:
        name = "users"

    class Config:
        schema_extra = {
            "example": {"ardaId":8716174,
                        "ggId":"1125867",
                        "name":"Kevin Bueno",
                        "comparableName":
                        "kevin bueno",
                        "username":
                        "aristotekean",
                        "professionalHeadline":"Software Engineer",
                        "imageUrl":"https://res.cloudinary.com/torre-technologies-co/image/upload/c_fill,h_150,w_150/v1659907802/origin/starrgate/users/profile_2c1fa79323cbbd980c0b74da81ed08acf8101c9f.jpg",
                        "completion":0.8889,
                        "grammar":0.57895,
                        "weight":0.0,
                        "verified":True,
                        "connections":[],
                        "totalStrength":0.0,
                        "pageRank":0.15000000000000002,
                        "organizationId":None,
                        "organizationNumericId":None,
                        "publicId":None,
                        "status":None,
                        "creators":[],
                        "relationDegree":1,
                        "contact":False}
        }

    

class UserResponse(UserBase):
    pass