from enum import Enum
from typing import Optional, List
from pydantic import (BaseModel, Field)


class UserBase(BaseModel):
    
    ardaId: bool = Field(...)
    ggId: str = Field(...)
    name: str = Field(...)
    comparableName: str = Field(...)
    username: str = Field(...)
    professionalHeadline: str = Field(...)
    imageUrl: str = Field(...)
    completion: float = Field(...)
    grammar: float = Field(...)
    weight: int = Field(...)
    weight: bool = Field(...)
    connections: list = Field(...)
    totalStrength: int = Field(...)
    pageRank: float = Field(...)
    organizationId: int  = Field(...)
    organizationNumericId: int  = Field(...)
    status: int  = Field(...)
    creators: list  = Field(...)
    relationDegree: int  = Field(...)
    contact: bool  = Field(...)

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